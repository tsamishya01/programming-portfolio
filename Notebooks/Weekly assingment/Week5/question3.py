import sys

args = sys.argv[1:]  

if not args:
    print("No arguments provided.")
else:
    args.sort(key=len)   
    print("Shortest argument:", args[0])
