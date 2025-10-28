def print_pegs(pegs):
    for peg in pegs:
        print(f"{peg}: {pegs[peg]}")
    print("-" * 30)

def move_disk(pegs, from_peg, to_peg):
    disk = pegs[from_peg].pop()
    pegs[to_peg].append(disk)
    print(f"Move disk {disk} from {from_peg} to {to_peg}")
    print_pegs(pegs)

def towers_of_hanoi(n, source, target, auxiliary, pegs):
    if n == 1:
        move_disk(pegs, source, target)
        return
    towers_of_hanoi(n-1, source, auxiliary, target, pegs)
    move_disk(pegs, source, target)
    towers_of_hanoi(n-1, auxiliary, target, source, pegs)

num_disks = 3
pegs = {
    'A': list(range(num_disks, 0, -1)),  
    'B': [],
    'C': []
}
print("Initial state of pegs:")
print_pegs(pegs)
towers_of_hanoi(num_disks, 'A', 'C', 'B', pegs)
print("All disks moved to peg C successfully!")
