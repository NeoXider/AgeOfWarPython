# AgeOfWarPython — примеры и паттерны

Этот файл — “шпаргалка” по тому, **как правильно расширять** проект.

## Полный пример: как добавить систему (от и до)

Цель примера: добавить систему `CounterSystem`, которая раз в секунду увеличивает счётчик и шлёт событие, а `UISystem` ловит событие и обновляет текст.

### Шаг 1. Добавляем событие и payload в `game/global_events.py`

```python
class GameEvents:
    COUNTER_CHANGED = "aow.counter.changed"

@dataclass(frozen=True, slots=True)
class CounterChanged:
    value: int
```

Правило проекта: отправляем всегда через `data=...`:

```python
s.events.send(GameEvents.COUNTER_CHANGED, data=CounterChanged(value=123))
```

### Шаг 2. Создаём систему в `game/systems/counter_system.py`

```python
from game.global_events import GameEvents, CounterChanged

class CounterSystem:
    def __init__(self, events, tick_seconds: float = 1.0) -> None:
        self._events = events  # обычно s.events
        self._tick = tick_seconds
        self._acc = 0.0
        self._value = 0

    def on_enter(self) -> None:
        self._acc = 0.0
        self._value = 0

    def on_exit(self) -> None:
        pass

    def update(self, dt: float) -> None:
        self._acc += max(0.0, dt)
        while self._acc >= self._tick:
            self._acc -= self._tick
            self._value += 1
            self._events.send(
                GameEvents.COUNTER_CHANGED,
                data=CounterChanged(value=self._value),
            )
```

### Шаг 3. Подключаем систему в `GameScene`

Добавляем систему в список `self.systems` в `game/scenes/game_scene.py`:

```python
from game.systems.counter_system import CounterSystem

self.systems = [
    EconomySystem(self.events, self.economy),
    SpawnSystem(self.events, units=self.units, scene=self),
    BattleSystem(self.events, units=self.units, projectiles=self.projectiles),
    CounterSystem(self.events),
    UISystem(self.events, scene=self),
]
```

Важно: система должна появиться **до** `UISystem`, если UI ожидает события сразу после старта (не всегда обязательно, но проще для понимания).

### Шаг 4. UI подписывается на событие и обновляет текст

Пример “как UI должен ловить событие” (функция-обработчик + connect/disconnect). Логика живёт в `UISystem`:

```python
from game.global_events import GameEvents, CounterChanged

class UISystem:
    def __init__(self, events, *, scene):
        self._events = events
        self._scene = scene
        self._counter_handler = None
        self._counter_text = None

    def on_enter(self):
        self._counter_text = s.TextSprite("Counter: 0", 24, (255, 255, 255), (10, 40), scene=self._scene)
        self._counter_text.set_screen_space(True)

        # Подписка
        self._events.connect(GameEvents.COUNTER_CHANGED, self._on_counter_changed)
        self._counter_handler = self._on_counter_changed

    def on_exit(self):
        # Отписка
        if self._counter_handler:
            self._events.disconnect(GameEvents.COUNTER_CHANGED, self._counter_handler)
            self._counter_handler = None

    def _on_counter_changed(self, *, data: CounterChanged) -> None:
        if self._counter_text:
            self._counter_text.set_text(f"Counter: {data.value}")
```

Ключевые правила:

- **обработчик должен совпадать по сигнатуре**: `def handler(self, *, data: Payload)`
- **подписку обязательно снимать** в `on_exit()` через `disconnect`

## Мини-шаблон: как добавлять ассеты (через `paths.py`)

Если вы создали новую папку, например `assets/ui/`, то:

1) Добавьте поле в `game/paths.py`
2) В коде используйте `PATHS.ui`, а не `"assets/ui"`

## Чеклист: как делать фичу “от и до”

1) **Сформулировать**: что делаем и где это живёт (Scene/System/Entity/Domain)
2) **Домен**: добавить данные/правила (если нужно) в `game/domain/`
3) **События**: определить событие в `game/global_events.py` (имя + payload)
4) **Система**: реализовать логику (update + send)
5) **UI**: подписаться на событие (connect/handler/disconnect)
6) **Интеграция**: подключить систему в `GameScene.systems`
7) **Тест-план**: написать 3–5 шагов ручной проверки
8) **TASKS.md**: если фича большая — разбить на таски и дать номера
