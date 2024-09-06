
# Print the pattern
msg = []
for i in range(10):
    if i <= 4:
        msg.append('*')
    else: 
        msg.remove('*')
    print(' '.join(msg))