class PerformanceBenchmark:

    def __init__(
        self,
        pipeline,
        dataset,
        optim_type
        ):
        self.pipeline = pipeline
        self.dataset = dataset
        self.optim_type = optim_type

    def compute_size(self):
        pass

    def compute_accuracy(self):
        pass

    def compute_latency(self):
        pass

    def compute_benchmark(self):
        metric = {}
        metric[self.optim_type] = self.compute_size()
        metric[self.optim_type].update(self.compute_accuracy())
        metric[self.optim_type].update(self.compute_latency())
        return metric


