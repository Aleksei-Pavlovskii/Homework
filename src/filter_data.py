def filter_data_file(data: list[dict]) -> list[dict]:
    """Функция, которая приводит список словарей к единому виду"""
    file = []

    for transaction in data:
        converted_dict = {
            "amount": transaction.get("operationAmount", {}).get("amount") or transaction.get("amount"),
            "currency_code": transaction.get("operationAmount", {}).get("currency", {}).get("code")
            or transaction.get("currency", {}),
            "currency_name": transaction.get("operationAmount", {}).get("currency", {}).get("name")
            or transaction.get("currency_name"),
            "date": transaction.get("date"),
            "description": transaction.get("description"),
            "from": transaction.get("from"),
            "id": transaction.get("id"),
            "state": transaction.get("state"),
            "to": transaction.get("to"),
        }
        file.append(converted_dict)
    return file
