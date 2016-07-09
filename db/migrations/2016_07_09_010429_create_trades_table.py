from orator.migrations import Migration


class CreateTradesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('trades') as table:
            table.increments('id')
            table.integer('stock_portfolio_id').unsigned()
            table.foreign('stock_portfolio_id').references('id').on('stocks_portfolios') 
            table.date('date')
            table.integer('quantity')
            table.double('price', 15, 8)
            table.timestamps(use_current=True)

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('trades')
