import datetime
from decimal import Decimal
DATE_FORMAT = '%Y-%m-%d'
goods = {
    'Пельмени Универсальные': [
        {'amount': Decimal('0.5'), 'expiration_date': datetime.date(2023, 7, 15)},
        {'amount': Decimal('2'), 'expiration_date': datetime.date(2023, 8, 1)},
    ],
    'Вода': [
        {'amount': Decimal('1.5'), 'expiration_date': None}
    ],
}
def add(items, title, amount, expiration_date=None):
    if isinstance(expiration_date, str):
        expiration_date = datetime.datetime.strptime(expiration_date, DATE_FORMAT).date()
    if title in items:
        items[title].append({'amount': amount, 'expiration_date': expiration_date})
    else:
        items[title] = [{'amount': amount, 'expiration_date': expiration_date}]
def add_by_note(items, note):
    parts = note.split()
    last = parts[-1]
    if '-' in last:
        expiration_date = last
        amount = Decimal(parts[-2])
        title = ' '.join(parts[:-2])
    else:
        expiration_date = None
        amount = Decimal(last)
        title = ' '.join(parts[:-1])
    add(items, title, amount, expiration_date)
def find(items, needle):
    result = []
    for product in items:
        if needle.lower() in product.lower():
            result.append(product)
    return result
def get_amount(items, needle):
    total = Decimal('0')
    for title in find(items, needle):
        for batch in items[title]:
            total += batch['amount']
    return total
def get_expired(items, in_advance_days=0):
    if in_advance_days is None:
        in_advance_days = 0
    today = datetime.date.today()
    critical_date = today + datetime.timedelta(days=in_advance_days)
    result = {}
    for product in items:
        for batch in items[product]:
            date = batch['expiration_date']
            if date is not None and date <= critical_date:
                if product not in result:
                    result[product] = Decimal('0')
                result[product] += batch['amount']
    return list(result.items())
