cricketers = [18, 'Virat Kohli', 7, 'MS Dhoni', 45, 'Rohit Sharma', 10, 'Sachin Tendulkar']
nums = [x for x in cricketers if type(x) == int]
print(sum(nums))