from code.background import background
from code.const import WIN_WIDH


class entityFactory:

    @staticmethod
    def get_entity(entity_name:str, position=(0,0)):

        match entity_name:
            case 'Level1Bg':
                listBg=[]
                for i in range(7):
                    listBg.append(background(f'Level1Bg{i}',(0,0)))
                    listBg.append(background(f'Level1Bg{i}', (WIN_WIDH, 0)))
                return listBg


