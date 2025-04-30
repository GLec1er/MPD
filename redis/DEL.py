# 1. Атомарное удаление одного ключа
# Если нужно просто удалить один ключ, можно использовать команду DEL. Эта команда выполняется атомарно, то есть гарантирует,
# что ключ будет удален без риска конфликтов с другими операциями.

async def delete_key_from_redis(key):
    """
    Удаляет ключ из Redis атомарно.
    """
    try:
        # Удаляем ключ атомарно
        result = await redis.delete(key)
        return result  # Возвращает количество удаленных ключей (0 или 1)
    except Exception as e:
        print(f"Ошибка при удалении ключа {key}: {e}")
        raise

# 2. Атомарное удаление с использованием транзакций

# Если нужно выполнить несколько связанных операций (например, проверить значение, обновить его и затем удалить), можно
# использовать транзакции Redis через MULTI/EXEC. В Python это поддерживается библиотекой aioredis через контекстный менеджер redis.multi_exec().

async def transactional_delete_key(redis, key, expected_value):
    """
    Удаляет ключ атомарно, только если его значение равно expected_value,
    используя транзакцию Redis.
    """
    try:
        async with redis.multi_exec() as multi:
            # Получаем текущее значение ключа
            current_value = await redis.get(key)

            # Проверяем, соответствует ли значение ожидаемому
            if current_value and current_value.decode() == expected_value:
                # Удаляем ключ
                multi.delete(key)
            else:
                # Ничего не делаем
                pass

        # Транзакция завершена
        return True
    except Exception as e:
        print(f"Ошибка при выполнении транзакции: {e}")
        raise