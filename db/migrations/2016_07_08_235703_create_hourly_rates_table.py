from orator.migrations import Migration


class CreateHourlyRatesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('hourly_rates') as table:
            table.increments('id')
            table.double('price')
            table.date('date')
            table.integer('stock_id').unsigned()
            table.foreign('stock_id').references('id').on('stocks')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('hourly_rates')
