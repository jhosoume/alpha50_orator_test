from orator.migrations import Migration


class CreateMinuteQuotesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('minute_quotes') as table:
            table.increments('id')
            table.float('price')
            table.datetime('datetime')
            table.integer('stock_id').unsigned()
            table.foreign('stock_id').references('id').on('stocks')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('minute_quotes')
