import web
import matalyst.numbers.validation
import matalyst.numbers.factorization
web.config.debug=True
urls = (
	'/matalyst/numbers/validation/is-integer', 'matalyst.numbers.validation.IsInteger',
	'/matalyst/numbers/factorization/get', 'matalyst.numbers.factorization.Get',
	'/matalyst/list/sorting/ascending', 'matalyst.list.sorting.Ascending',
)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
