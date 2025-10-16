import pygame

class Tilemap:
    def __init__(self, game,  tile_size = 32):
        self.game = game
        self.tile_size = tile_size
        self.tilemap = {}
        self.offgrid_tiles = []
        self.rects = []

        for i in range(0, 10, 2):
            self.tilemap[str(5+i) + ';4'] = {
                'type': 'dirt', 
                'pos' : (5 + i, 4), 
                'rect': pygame.Rect( (5 + i) * tile_size, 4 * tile_size, self.tile_size, self.tile_size),
                'timer': 0}
            
            self.tilemap[str(5+i) + ';8'] = { 
                'type': 'dirt', 
                'pos': (5 + i, 8),
                'rect': pygame.Rect( (5 + i) * tile_size, 8 * tile_size, self.tile_size, self.tile_size),
                'timer': 0}
            
            self.tilemap[str(5+i) + ';12'] = { 
                'type': 'dirt',
                'pos': (5 + i, 12),
                'rect': pygame.Rect( (5 + i) * tile_size, 12 * tile_size, self.tile_size, self.tile_size),
                'timer': 0}

            
        self.get_rects()

    def get_rects(self):
        self.rects = []
        for key, value in self.tilemap.items():
            x, y = value['pos']
            rect = pygame.Rect(x* self.tile_size, y * self.tile_size, self.tile_size, self.tile_size)
            self.rects.append(rect)
            
    def render(self, surf):
        for key, value in self.tilemap.items():
            x, y = value['pos']      
            rect = pygame.Rect(x* self.tile_size, y * self.tile_size, self.tile_size, self.tile_size)
            pygame.draw.rect(surf, (155, 75, 0), rect)

            if(value['type'] == 'seed' or value['type'] == 'seed_growing'):
                offset = self.tile_size // 2.5
                small_rect = pygame.Rect(x* self.tile_size + offset, y * self.tile_size + offset,  (self.tile_size) / 4, (self.tile_size) / 4)
                pygame.draw.rect(surf, (0, 255, 0), small_rect)
            elif (value['type'] == 'sprout' or value['type'] == 'sprout_growing') :
                offset = self.tile_size // 4
                medium_rect = pygame.Rect(x* self.tile_size + offset, y * self.tile_size + offset,  (self.tile_size) / 2, (self.tile_size) / 2)
                pygame.draw.rect(surf, (0, 255, 0), medium_rect)
            elif (value['type'] == 'grown'):
                rect = pygame.Rect(x* self.tile_size, y * self.tile_size, self.tile_size, self.tile_size)
                pygame.draw.rect(surf, (0, 255, 0), rect)

    


           
    