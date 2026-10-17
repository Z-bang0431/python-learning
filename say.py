import cowsay
import sys 

if len(sys.argv) == 2:
    # cowsay.cow("hello," + sys.argv[1])  # cowsay.cow呈现出牛，trex呈现霸王龙
    cowsay.trex("hello," + sys.argv[1])