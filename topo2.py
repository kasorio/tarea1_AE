from mininet.topo import Topo

class MyTopo(Topo):
    "Custom topology example."

    def build(self):
        "Create custom topo."

        # Add hosts and switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')

        h1 = self.addHost('h1')
        h2 = self.addHost('h2')

        # Add links with custom properties
        self.addLink(s1, s2, bw=5 , delay='50ms', loss=2)
        self.addLink(s2, s3, bw=10, delay='70ms', loss=2)
        self.addLink(s3, s4, bw=5, delay='30ms', loss=2)

        self.addLink(h1, s1)
        self.addLink(h2, s4)

topos = {'mytopo': (lambda: MyTopo())}
