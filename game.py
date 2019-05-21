import pygame
from targets import target
pygame.init()

targetList = []
class game(object):
    def __init__(self):
        self.score = 1
        self.size = self.width, self.height = (700, 700)
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption('Aim Trainer')
        self.font = pygame.font.SysFont('comicsans', 30, True)
        self.targetCount = 0

    def gameLoop(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    clickPos = pygame.mouse.get_pos()
                    print(clickPos)
                    for blob in targetList:
                        if blob.clickDetection(clickPos):
                            print('HIT')
                            blob.targetHit = True
                            targetList.pop(targetList.index(blob))
                            self.score += 1

            self.getTargets()
            self.increaseTargetSize()
            self.redrawWindow()

    def increaseTargetSize(self):
        for blob in targetList:
            blob.setNewRadius(2)

    def getTargets(self):
        if len(targetList) <= 5:
            targetList.append(target(20, self.width, self.height))
        else:
            targetList.pop(0)
            self.score -= 1
            # Decrease score

    def redrawWindow(self):
        self.screen.fill((0, 0, 0))
        scoreText = self.font.render('Score: ' + str(self.score), 1, (255, 0, 0))
        self.screen.blit(scoreText, (self.width - 200, 10))

        for blobs in targetList:
            if blobs.targetHit == True:
                blobs.draw(self.screen, (255, 0, 0))
            else:
                blobs.draw(self.screen, (0, 225, 0))

        pygame.display.update()  # Update the window

startGame = game()
startGame.gameLoop()

# Quit game, uninitialize all elements
pygame.quit()
