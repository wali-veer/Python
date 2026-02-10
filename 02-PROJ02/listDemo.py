row = ['Jeep','Kia','Maruti','honda']
print(f'Original --> {str(row)}')

row.append('Volk Wagen')
print(f'append --> {str(row)}')

row[2]='Tata'
print(f'Over write 2 --> {str(row)}')

row.insert(0,'Mahindra')
print(f'insert at 0 --> {str(row)}')

print(f'index of Tata --> {row.index('Tata')}')
print(f'Remove Tata --> {row.pop(3)}')
print(f'After Remove Tata --> {str(row)}')

row.remove('honda')
print(f'After Remove honda --> {str(row)}')