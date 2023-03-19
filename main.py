# python3

def parallel_processing(n, m, data):
    output = []
    processing = []
    threads = []
    
    for i in range(n):
        processing.append(0)
        threads.append(i)
    
    for i in range(m):
        min_processing = min(processing)
        min_threads = processing.index(min_processing)
        output.append((min_threads, min_processing))
        processing[min_threads] += data[i]

    return output

def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    result = parallel_processing(n,m,data)
    
    for thread_index, start_time in result:
        print(thread_index, start_time)



if __name__ == "__main__":
    main()
