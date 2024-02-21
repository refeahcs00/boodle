import os
import yaml

from src.user import User

BANNER_SLANT = '''
    ____  ____  ____  ____  __    ______
   / __ )/ __ \/ __ \/ __ \/ /   / ____/
  / __  / / / / / / / / / / /   / __/   
 / /_/ / /_/ / /_/ / /_/ / /___/ /___   
/_____/\____/\____/_____/_____/_____/   
                                        
'''

BANNER_3D = '''
                                                       ,--,
               ,----..       ,----..                ,---.'|
    ,---,.    /   /   \     /   /   \      ,---,    |   | :       ,---,.
  ,'  .'  \  /   .     :   /   .     :   .'  .' `\  :   : |     ,'  .' |
,---.' .' | .   /   ;.  \ .   /   ;.  \,---.'     \ |   ' :   ,---.'   |
|   |  |: |.   ;   /  ` ;.   ;   /  ` ;|   |  .`\  |;   ; '   |   |   .'
:   :  :  /;   |  ; \ ; |;   |  ; \ ; |:   : |  '  |'   | |__ :   :  |-,
:   |    ; |   :  | ; | '|   :  | ; | '|   ' '  ;  :|   | :.'|:   |  ;/|
|   :     \.   |  ' ' ' :.   |  ' ' ' :'   | ;  .  |'   :    ;|   :   .'
|   |   . |'   ;  \; /  |'   ;  \; /  ||   | :  |  '|   |  ./ |   |  |-,
'   :  '; | \   \  ',  /  \   \  ',  / '   : | /  ; ;   : ;   '   :  ;/|
|   |  | ;   ;   :    /    ;   :    /  |   | '` ,/  |   ,/    |   |    \\
|   :   /     \   \ .'      \   \ .'   ;   :  .'    '---'     |   :   .'
|   | ,'       `---`         `---`     |   ,.'                |   | ,'
`----'                                 '---'                  `----'
'''


if __name__ == '__main__':
    print(BANNER_3D)
    print('v 0.0.1 - 2024-02-20')

    user = User()
