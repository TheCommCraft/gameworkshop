import gameworkshop
import gameworkshop.game_state
import gameworkshop.grid
import gameworkshop.consts

gs = gameworkshop.game_state.GameState()
gs.init()
obj = gameworkshop.grid.Grid(gameworkshop.consts.SCREEN_WIDTH // 32, gameworkshop.consts.SCREEN_HEIGHT // 32)
gs.add_obj(obj)
gs.start()