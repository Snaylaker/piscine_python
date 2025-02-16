def ft_tqdm(lst: range) -> None:
    valid = range(0, lst.stop+int(lst.stop*0.05), int(lst.stop*0.05))

    def percantage(i): return str(valid.index(i)*5) + "%|"

    def progressBar(i): return "█" * valid.index(i) + " " * \
        (valid.__len__() - valid.index(i)) + "|"

    def progressNumber(i): return str(i)+"/"+str(lst.stop)

    for i in lst:
        if i in valid:
            print(percantage(i), progressBar(i), progressNumber(
                i), end='\r',  flush=True, sep='')
        yield i
