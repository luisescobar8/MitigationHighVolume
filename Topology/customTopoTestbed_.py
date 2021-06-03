"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        h1 = self.addHost( 'h1' ) # 
        h2 = self.addHost( 'h2' ) # 
        h3 = self.addHost( 'h3' ) # 
        h4 = self.addHost( 'h4' ) # 
        h5 = self.addHost( 'h5' ) # 
        h6 = self.addHost( 'h6' ) # 
        h7 = self.addHost( 'h7' ) # 
        h8 = self.addHost( 'h8' ) # 
        h9 = self.addHost( 'h9' ) # 
        h10 = self.addHost( 'h10' ) # 
        h11 = self.addHost( 'h11' ) # 
        h12 = self.addHost( 'h12' ) # 
        h13 = self.addHost( 'h13' ) # 
        h14 = self.addHost( 'h14' ) # 
        h15 = self.addHost( 'h15' ) # 
        h16 = self.addHost( 'h16' ) # 

        SW1 = self.addSwitch( 's1')
        SW2 = self.addSwitch( 's2')
        SW3 = self.addSwitch( 's3' )
        SW4 = self.addSwitch( 's4' )
        SW5 = self.addSwitch( 's5' )
        

        # mirror server
        SW101 = self.addSwitch('s101')
        h101    = self.addHost( 'h101' ) 
        self.addLink( SW101, h101)  
        self.addLink( SW1, SW101)
        self.addLink( SW2, SW101)
        self.addLink( SW3, SW101)
        self.addLink( SW4, SW101)
        self.addLink( SW5, SW101)

        # Add links in tree topology
        self.addLink( SW1, SW2)
        self.addLink( SW1, SW3)
        self.addLink( SW1, SW4)
        self.addLink( SW1, SW5)
        self.addLink( SW3, SW2)
        self.addLink( SW4, SW3)
        self.addLink( SW5, SW4)
        self.addLink( SW2, SW5)
        self.addLink( SW2, h1)  #
        self.addLink( SW2, h2)  #
        self.addLink( SW2, h3)  #
        self.addLink( SW2, h4)  #
        self.addLink( SW3, h5)  #
        self.addLink( SW3, h6)  #
        self.addLink( SW3, h7)  #
        self.addLink( SW3, h8)  #
        self.addLink( SW4, h9)  #
        self.addLink( SW4, h10)  #
        self.addLink( SW4, h11)  #
        self.addLink( SW4, h12)  #
        self.addLink( SW5, h13)  #
        self.addLink( SW5, h14)  #
        self.addLink( SW5, h15)  #
        self.addLink( SW5, h16)  #


        
topos = { 'mytopo': ( lambda: MyTopo() ) }