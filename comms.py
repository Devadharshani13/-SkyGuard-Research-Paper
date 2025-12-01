"""
ZeroMQ-backed communications with optional latency & packet-loss simulation.
This file exports SimpleComms (PUB only for demo) and ZmqComms (PUB/SUB).
"""
import time
import random
import json

# Lightweight stub used by demo (no network)
class SimpleComms:
    def publish(self, topic, data):
        # no-op in demo (local)
        return

# Optional ZeroMQ comms - use if you want process separation
try:
    import zmq
    class ZmqComms:
        def __init__(self, pub_port=5555, latency=0.0, loss_prob=0.0):
            self.ctx = zmq.Context()
            self.pub = self.ctx.socket(zmq.PUB)
            self.pub.bind(f"tcp://*:{pub_port}")
            self.latency = latency
            self.loss_prob = loss_prob

        def publish(self, topic, data):
            if random.random() < self.loss_prob:
                return
            if self.latency > 0:
                time.sleep(self.latency)
            self.pub.send_string(topic + ' ' + json.dumps(data))
except Exception:
    ZmqComms = None
