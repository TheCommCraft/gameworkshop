import gameworkshop
import gameworkshop.game_state
import gameworkshop.grid
import gameworkshop.consts
import gameworkshop.player

gs = gameworkshop.game_state.GameState()
gs.init()
grid = gameworkshop.grid.Grid(gameworkshop.consts.SCREEN_WIDTH // gameworkshop.consts.TILE_SIZE, gameworkshop.consts.SCREEN_HEIGHT // gameworkshop.consts.TILE_SIZE)
gs.add_obj(grid)
player = gameworkshop.player.Player(20, 20, grid)
gs.add_obj(player)
gs.start()