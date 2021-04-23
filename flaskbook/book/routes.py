from .book import BooksApi, BookApi

def initialize_routes(api):
 # api.add_resource(MoviesApi, '/movies')
 # api.add_resource(MovieApi, '/movies/<id>')
  api.add_resource(BooksApi, '/api/books')
  api.add_resource(BookApi, '/api/books/<id>')