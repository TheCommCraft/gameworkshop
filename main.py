import gameworkshop
import gameworkshop.game_state
import gameworkshop.grid

gs = gameworkshop.game_state.GameState()
gs.init()
obj = gameworkshop.grid.Grid(10, 10)
gs.add_obj(obj)
gs.start()