
reticulate::repl_python()

from vetiver import VetiverModel
from vetiver import VetiverAPI
import pins

b = pins.board_folder(path = 'data/model', allow_pickle_read = True)
v = VetiverModel.from_pin(board = b, name = 'penguin_model')

api = VetiverAPI(model = v, check_prototype = True)
api.run(port = 8080)

exit
