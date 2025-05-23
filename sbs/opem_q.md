# Вопрос №1 Опыт работы с асинкой потоками и процессами

1. про потоки можно сказать про десктопные приложения на питоне то есть когда потом бэкенад и визуал не согласованны и получаются визуальные баги

2. про процессы можно сказать про опыт использвания процессов для email рассылки

3. про асинхронность когда использовалось либа с синхронным кодом по типу request

___

# Вопрос №2 Расскажи про опыт использования декораторов


Декоратор setattr_decorator в этом коде — это механизм ленивого вычисления (lazy evaluation) с кэшированием результата.

### ❓ В чём суть проблемы, которую он решает?
Когда ты работаешь с @property, каждый вызов свойства вызывает метод снова и снова. Если метод обращается к БД (как get_object_or_404) или вычисляет что-то нетривиальное, это дорого по ресурсам.

### ✅ Что делает setattr_decorator?
Впервые при обращении к свойству:

1. вызывает функцию (например, review_user()),
2. сохраняет результат в приватный атрибут (self._review_user).

Все последующие обращения просто читают это значение:

```python
return getattr(self, "_review_user")  # Уже сохранено
```

### 🔍 Что это даёт?
1. Экономия ресурсов — нет повторных запросов в БД.

2. Простота использования — внешний интерфейс остаётся @property, никаких @cached_property, lru_cache, или явного сохранения результата.

3. Контроль — ты сам указываешь, какие свойства нужно кэшировать и где хранятся результаты (__slots__ защищают от опечаток и лишних атрибутов).

### 📌 Почему не @cached_property?
1. @cached_property работает только на уровне класса, и только один раз.

2. В этом же миксине свойства можно сбросить вручную (например, обнулив _review_user).

3. @cached_property не совместим с __slots__ без дополнительных трюков.
