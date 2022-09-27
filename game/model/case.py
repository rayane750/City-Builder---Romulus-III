class Case:
    def __init__(self, grid, cart_rect, iso_poly, render_pos, tile):
        self.grid = grid
        self.cart_rect = cart_rect
        self.iso_poly = iso_poly
        self.render_pos = render_pos
        self.tile = tile
        self.entites = []

    def get_grid(self):
        return self.grid

    def get_cart_rect(self):
        return self.cart_rect

    def get_iso_poly(self):
        return self.iso_poly

    def get_render_pos(self):
        return self.render_pos

    def get_tile(self):
        return self.tile

    def get_entities(self):
        return self.entites