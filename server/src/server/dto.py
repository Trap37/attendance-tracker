class GearStats:
    @staticmethod
    def stats():
        # TODO: Get data from database
        gear_stats = {
            'total': 0,
            'keyboards': 0,
            'mice': 0,
            'other_gear': 0,
        }
        return gear_stats

    @staticmethod
    def checkouts():
        # TODO: Get data from database
        checkouts = [
            {
                'checkout_id': '1',
                'scan_id': '12345',
                'full_name': 'John Doe',
                'items': [
                    'total',
                    'keyboards',
                    'mice',
                    'other_gear',
                ],
                'Checkout Time': '2023-06-01 10:00:00',
            }
        ]

        return checkouts


for row in GearStats.checkouts():
    print(type(row['items']))
