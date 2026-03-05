input_file = "C:/Users/Akshayaa/Downloads/archive (7)/HDFS_2k/HDFS_2k.log"
output_file = "logs.txt"

count = 0
limit = 2000

with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    for line in infile:
        outfile.write(line)
        count += 1
        if count >= limit:
            break

print("2000 logs extracted successfully")