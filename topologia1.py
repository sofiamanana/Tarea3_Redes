from mininet.topo import Topo

class Tp1 ( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        h1 = self.addHost( 'h1', mac = '00:00:00:00:00:01' )
        h2 = self.addHost( 'h2', mac = '00:00:00:00:00:02'  )
        h3 = self.addHost( 'h3', mac = '00:00:00:00:00:03'  )
        h4 = self.addHost( 'h4', mac = '00:00:00:00:00:04'  )
        h5 = self.addHost( 'h5', mac = '00:00:00:00:00:05'  )
        h6 = self.addHost( 'h6', mac = '00:00:00:00:00:06'  )
        h7 = self.addHost( 'h7', mac = '00:00:00:00:00:07'  )
        h8 = self.addHost( 'h8', mac = '00:00:00:00:00:08'  )
             
        s1 = self.addSwitch( 's1' )
        s2 = self.addSwitch( 's2' )
        s3 = self.addSwitch( 's3' )
        s4 = self.addSwitch( 's4' )

        # Add links
        self.addLink( h1, s1,1,2)#ha 1 => 2 sx
        self.addLink( h2, s1, 3,4)#hb 3 => 4 sx
        self.addLink( h3, s2,5,6 )#hc 5 => 6 sy
        self.addLink( h4, s2,7,8 )# hd 7 => 8 sy
        self.addLink( h5, s3,9,10 )#he 9 => 10 sz
        self.addLink( h6, s3,11,12 )#hf 11 => 12 sz
        self.addLink( h7, s4,13,14 )#Sx 13 => 14 Sy
        self.addLink( h8, s4,15,16 )#Sx 15 => 16 Sz
        self.addLink( s1, s2,17,18 )#Sy 17 => 18 Sz
        self.addLink( s2, s3,19,20 )#Sy 17 => 18 Sz
        self.addLink( s1, s4,21,22 )#Sy 17 => 18 Sz
        self.addLink( s3, s4,23,24 )#Sy 17 => 18 Sz


topos = { 'tp1': ( lambda: Tp1() ) }