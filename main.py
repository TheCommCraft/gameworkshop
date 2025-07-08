import gameworkshop
import gameworkshop.game_state
import gameworkshop.grid
import gameworkshop.consts

gs = gameworkshop.game_state.GameState()
gs.init()
obj = gameworkshop.grid.Grid(gameworkshop.consts.SCREEN_WIDTH // gameworkshop.consts.TILE_SIZE, gameworkshop.consts.SCREEN_HEIGHT // gameworkshop.consts.TILE_SIZE)
gs.add_obj(obj)
gs.start()