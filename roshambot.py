
import random
import cmath
import numpy as np
from cmath import *

class game_master:
    """
    A and B are two RPS objects which will play against each other.
    """
    def __init__(self, A, B, ngames=1001, early_end=False):
        self.score=[0,0]
        self.move_list=[ '', '' ]
        self.A=A
        self.B=B
        self.ngames=ngames
        self.moves='rps'
        self.trump={'r':'p', 'p':'s', 's':'r'}
        self.early_end=early_end

    def run_game(self):
        """
        Run N games between the two players.
        """
        for i in xrange(self.ngames):
            a_move=self.A.get_move()
            self.move_list[0]+=a_move
            b_move=self.B.get_move()
            self.move_list[1]+=b_move

            #Tell the players the outcomes.
            #Both players think they are player one.
            a_i=self.moves.index(a_move)
            b_j=self.moves.index(b_move)
            if (a_i-1)%3==b_j:
                self.score[0]+=1
                self.A.report( a_move, b_move, 1 )
                self.B.report( b_move, a_move, -1 )
            elif (a_i+1)%3==b_j:
                self.score[1]+=1
                self.A.report( a_move, b_move, -1 )
                self.B.report( b_move, a_move, 1 )
            else:
                self.A.report( a_move, b_move, 0 )
                self.B.report( b_move, a_move, 0 )
            if self.early_end and ( (self.score[0]>self.ngames/2) or (self.score[1]>self.ngames/2)):
                break
        return self.score

    def plot(self, colors=['red', 'blue'], interval=None):
        p=plot([])
        n=len(self.move_list[0])
        if interval==None: 
            if n>=100: 
                interval=int(0.01*n)
            else:
                interval=1
        running_score=[0,0]
        last_a_point=(0,0)
        last_b_point=(0,0)
        a_point=(0,0)
        b_point=(0,0)
        for i in range(n):
            a=self.move_list[0][i]
            b=self.move_list[1][i]
            if a==self.trump[b]:
                running_score[0]+=1
            elif b==self.trump[a]:
                running_score[1]+=1
            s=sum(running_score)
            if i%interval==0 and s!=0 and i>0:
                last_a_point=a_point
                last_b_point=b_point
                a_point=(i, 1.0*running_score[0]/s)
                b_point=(i, 1.0*running_score[1]/s)
                p+=point2d( a_point, color='red')
                p+=line2d( (last_a_point, a_point), color=colors[0] )
                p+=point2d( b_point, color='blue')
                p+=line2d( (last_b_point, b_point), color=colors[1] )
        return p

    def trial(self, n=10):
        game_wins=[0,0]
        for i in range(n):
            A.__init__()
            B.__init__()
            self.score=[0,0]
            self.run_game()
            if score[0]>score[1]:
                game_wins[0]+=1
            else:
                game_wins[1]+=1
        return game_wins

#-------------------------------------------------------------------------------
#----RPS players.
#-------------------------------------------------------------------------------

#TODO: Probably the morally right thing to do would be to make an abstract class...

class rps_random:
    """
    This is our model for an RPS player, from which others inherit.
    The required methods for any player are `name`, `get_move`, and `report`.
    `name` gives a human-ish name to the bot, used in `__repr__` calls.
    `get_move` returns one of r,p,s.
    `report` is used by the `game_master` to report back the outcome of a move.
    """

    def __init__(self):
        self.move_list=[ '', '' ]
        self.score=[0,0]
        self.rps='rps'

    def name(self):
        """
        The `name` method gives the bot a name, used by `__repr__`.
        Or elsewhere, if you want.
        """
        return 'Randy'

    def __repr__(self):
        return 'A player named '+self.name()

    def trump(self, symbol):
        """
        Symbol is one of `r`, `p`, `s`.
        Return the symbol that beats provided symbol.
        """
        if symbol=='r': return 'p'
        if symbol=='p': return 's'
        if symbol=='s': return 'r'

    def get_move(self):
        """
        Choose a move.
        """
        return random.choice('rps')

    def report(self, my_move, opponent_move, outcome):
        """
        The `report` method allows the `game_master` to report the outcome of the
        last play.  The report consists of your move, the opponent's move, and
        who won.  (Which is redundant information, but so there.)
        """
        self.move_list[0]+=my_move
        self.move_list[1]+=opponent_move
        if outcome==1:
            self.score[0]+=1
        elif outcome==-1:
            self.score[1]+=1

#-------------------------------------------------------------------------------

class beat_last(rps_random):
    """
    Plays to beat the opponent's last move.  This is actually a pretty common
    pattern amongst flustered human players.

    Named Michael Jackson for 'Just Beat It'.
    """
    def name(self):
        return 'Michael Jackson'

    def get_move(self):
        """
        Choose a move.
        """
        if len(self.move_list[0])==0:
            return random.choice('rps')
        return self.trump(self.move_list[1][-1])

#-------------------------------------------------------------------------------

class reverse_beat_last(rps_random):
    """
    Like MJ, but plays to _lose_ to the last move played by the opponent.
    """
    def name(self):
        mj='noskcaJ leahciM'
        return mj

    def get_move(self):
        """
        Choose a move.
        """
        if len(self.move_list[0])==0:
            return random.choice('rps')
        return self.trump(self.trump(self.move_list[1][-1]))

#-------------------------------------------------------------------------------

class all_rock(rps_random):
    """
    Good ol' rock.  Nothing beats rock.
    """
    def name(self):
        return 'Bart Simpson'

    def get_move(self):
        """
        Choose a move.
        """
        return 'r'

#-------------------------------------------------------------------------------

class all_scissors(rps_random):
    """
    It's hard to have an interesting strategy when your hands are scissors.
    """
    def name(self):
        return 'Edward Scissorhands'

    def get_move(self):
        """
        Choose a move.
        """
        return 's'

#-------------------------------------------------------------------------------

class all_paper(rps_random):
    """
    Poor predicatble Bart.  Always plays rock.
    """
    def name(self):
        return 'Lisa Simpson'

    def get_move(self):
        """
        Choose a move.
        """
        return 'p'

#-------------------------------------------------------------------------------

class rock_622(rps_random):
    """
    Homer on the other hand has learned from experience, and only plays rock
    60% of the time, with his other plays split evenly between paper and scissors.
    """
    def name(self):
        return 'Smrt Homer'

    def get_move(self):
        """
        Choose a move.
        """
        x=random.random()
        if x<0.6: return 'r'
        if x<0.8: return 'p'
        return 's'

#-------------------------------------------------------------------------------

class random_bias(rps_random):
    """
    This bot generates a random bias at creation, and then takes rps at random
    according to the bias.
    """
    def name(self):
        return 'Random bias ' + str(tuple([round(x,2) for x in self.cutoffs]))

    def __init__(self):
        self.move_list=[ '', '' ]
        self.score=[0,0]
        self.rps='rps'
        self.cutoffs=[ random.random(), random.random() ]
        self.cutoffs.sort()
        self.cutoffs=tuple(self.cutoffs)

    def get_move(self):
        """
        Choose a move.
        """
        x=random.random()
        if x<self.cutoffs[0]: return 'r'
        if x>self.cutoffs[1]: return 's'
        return 'p'

#-------------------------------------------------------------------------------

class switchbot(rps_random):
    """
    Switchbot is a random bot, but never plays the same thing twice in a row.
    Also pretty common behaviour for humans...
    """
    def name(self):
        return 'Switchbot'

    def get_move(self):
        if len(self.move_list[0])==0: return random.choice('rps')
        a=self.move_list[0][-1]
        if a=='r': return random.choice('ps')
        if a=='p': return random.choice('rs')
        if a=='s': return random.choice('rp')

#-------------------------------------------------------------------------------

class counter_switchbot(rps_random):
    """
    Like switchbot, but plays anything except the opponent's last move.
    """
    def name(self):
        return 'Counter Switchbot'

    def get_move(self):
        if len(self.move_list[0])==0: return random.choice('rps')
        a=self.move_list[1][-1]
        if a=='r': return random.choice('ps')
        if a=='p': return random.choice('rs')
        if a=='s': return random.choice('rp')

#-------------------------------------------------------------------------------

class rfind(rps_random):
    """
    Search backwards through the move list for the longest possible string
    matching the current game state, and predict that the opponent will play
    the same way as before.

    This algorithm kills many learning algorithms, because learning algorithms
    'stabilize' and tend to play the same plays given the same data once
    they've seen enough data.
    """
    def name(self):
        return 'Rfind'

    def get_move(self):
        if len(self.move_list[0])==0: return random.choice('rps')
        #Kill last letter to avoid the trivial match.
        n=len(self.move_list[1])
        upper_bound=min(20, n-1)
        m=-1
        for k in range(upper_bound, 1, -1):
            match_string=self.move_list[1][-k:]
            m=self.move_list[1].rfind(match_string,0,-1)
            if m!=-1:
                break
        if m==-1: return random.choice('rps')
        return self.trump( self.move_list[1][m+k] )

#-------------------------------------------------------------------------------

class kcycle(rps_random):
    """
    Plays to beat move k steps ago from either own or opponent's move list.
    If beating own move list, this bot is periodic with period 3*k.

    `k` and `stream` are chosen randomly at startup, or can be selected.
    `k` is the length of cycle to use.
    `stream` should be 0 for the player's own move list, or 1 for the opponent's
    move list.
    """
    def name(self):
        return 'Lance '+str(self.k)+'-Strong '+str(self.stream)

    #Plays to beat most frequent opponent move.
    def __init__(self, k=None, stream=None):
        self.move_list=[ '', '' ]
        self.score=[0,0]
        self.moves='rps'
        self.opponent_move_totals=[0,0,0]
        if stream==None:
            self.stream=1
            if random.random()>.5: self.stream=0
        else:
            self.stream=stream
        if k==None:
            self.k=random.randint(1,50)
        else:
            self.k=k

    def get_move(self):
        if len(self.move_list[0])<self.k: return random.choice('rps')
        return self.trump( self.move_list[self.stream][-self.k] )

#-------------------------------------------------------------------------------

class freqbot(rps_random):
    """
    Simply plays to beat whatever the most frequent opponent move has been to
    this point.
    """
    def name(self):
        return 'Freqbot'

    def __init__(self):
        self.move_list=[ '', '' ]
        self.score=[0,0]
        self.moves='rps'
        self.opponent_move_totals=[0,0,0]

    def report(self, my_move, opponent_move, outcome):
        self.move_list[0]+=my_move
        self.move_list[1]+=opponent_move
        i=('rps').index(opponent_move)
        self.opponent_move_totals[i]+=1
        if outcome==1:
            self.score[0]+=1
        elif outcome==-1:
            self.score[1]+=1

    def get_move(self):
        if len(self.move_list[0])==0: return random.choice('rps')
        i=self.opponent_move_totals.index( max(self.opponent_move_totals) )
        if i==0: return 'p'
        if i==1: return 's'
        return 'r'

#-------------------------------------------------------------------------------

class humanbot(rps_random):
    """
    This is a bot with a fixed probability distribution based on gameplay of
    actual humans.  Probabilities are based on move sequences of maximum
    length five, which is certainly more than I can keep track of....
    """
    def name(self):
        return 'ho0m4nbot'

    def __init__(self):
        self.move_list=[ '', '' ]
        self.score=[0,0]
        self.moves='rps'
        f=file('openings.txt')
        R=[r.split('|') for r in f.readlines()][2:]
        move_totals=[ [0,0,0] for i in range(6) ]
        data=[ {} for i in range(6) ]
        for i in range(len(R)):
            R[i]=[ s.strip() for s in R[i] ]
            #n=number of moves in current sequence.
            n=len(R[i][0])
            for j in range(3): 
                R[i][j+2]=int(R[i][j+2])+1
            #Data file tracks info in order 'rsp' instead of 'rps'.  go figure.
            data[n][(R[i][0],R[i][1])]=(R[i][2],R[i][4],R[i][3])
            move_totals[n][0]+=R[i][2]
            move_totals[n][1]+=R[i][4]
            move_totals[n][2]+=R[i][3]
        self.move_totals=move_totals
        self.data=data

    def compute_probabilities(self):
        #Using Bayes' theorem, we get that:
        #  P(H|D) = #(observations of D and H) / #(observations of D)
        if len(self.move_list[1])<5:
            D=(self.move_list[0],self.move_list[1])
        else:
            D=(self.move_list[0][-5:],self.move_list[1][-5:])

        n=len(D[0])
        while not self.data[n].has_key(D):
            D=(D[0][1:], D[1][1:])
            n-=1
        if self.data[n].has_key(D):
            N = sum(self.data[n][D])
            P = [ 1.0*x/N for x in self.data[n][D] ]
            return P
        return [1.0/3 for i in range(3)]

    def get_move(self):
        P=self.compute_probabilities()
        #choose a random guess using probabilities.
        x=random.random()
        if x<P[0]: return 'r'
        if x<P[0]+P[1]: return 'p'
        return 's'

#-------------------------------------------------------------------------------

class terminator(humanbot):
    """
    A machine designed to kill humans.
    """
    def name(self):
        return 'Terminator'

    def compute_probabilities(self):
        #Use the same data as humanbot, but with relative roles reversed, so as
        #to come to the same decision as humanbot.
        if len(self.move_list[1])<5:
            D=(self.move_list[1],self.move_list[0])
        else:
            D=(self.move_list[1][-5:],self.move_list[0][-5:])

        n=len(D[0])
        while not self.data[n].has_key(D):
            D=(D[0][1:], D[1][1:])
            n-=1
        if self.data[n].has_key(D):
            N = sum(self.data[n][D])
            P = [ 1.0*x/N for x in self.data[n][D] ]
            return P
        return [1.0/3 for i in range(3)]

    def get_move(self):
        P=self.compute_probabilities()
        #choose a random guess using probabilities.
        x=random.random()
        if x<P[0]: return self.trump('r')
        if x<P[0]+P[1]: return self.trump('p')
        return self.trump('s')

#-------------------------------------------------------------------------------

class bayes(rps_random):
    """
    Keep track of all of opponent's k-move sequences and following moves.
    Use the collected data to estimate probability of each future move.
    Predict a move using the estimated probability distribution, then play
    the trumping move.

    Takes a 'memory' parameter which determines the length of history to keep track of.
    The number of tracked variables is exponential in the memory parameter;
    we create 3^(k+1) bins to track.
    This allows (much) better performance up to a point, but then drops off when
    the number of bins grows too large relative to the number of games played.
    """
    def __init__(self, memory=1):
        self.move_list=[ '', '' ]
        self.score=[0,0]
        self.moves='rps'
        #memory is the number of moves to keep track of in computing probabilities.
        #Our data requirements for high confidence are exponential in this variable,
        #but should eventually get better predictions with higher memory
        self.memory=memory
        last=['r', 'p', 's']
        mtuples=last[:]
        #Generate all rps tuples of length memory
        for i in xrange(self.memory-1):
            new=[]
            for a in last: new.append( 'r' + a )
            for a in last: new.append( 'p' + a )
            for a in last: new.append( 's' + a )
            last=new
        self.mtuples=last

        #Observed mtuples of opponent moves, initialized at one observation each.
        self.data={ a: [1,1,1] for a in self.mtuples }

    def name(self):
        return 'Bayes '+str(self.memory)

    def report(self, my_move, opponent_move, outcome):
        self.move_list[0]+=my_move
        self.move_list[1]+=opponent_move
        i=('rps').index(opponent_move)

        if outcome==1:
            self.score[0]+=1
        elif outcome==-1:
            self.score[1]+=1

        #Update data tables.
        if len(self.move_list[0])>self.memory:
            #m is the previous move
            new_data = self.move_list[1][-self.memory-1:-1]
            j='rps'.index( opponent_move )
            self.data[new_data][j]+=1

        if outcome==1:
            self.score[0]+=1
        elif outcome==-1:
            self.score[1]+=1

    def compute_probabilities(self):
        #Using Bayes' theorem, we get that:
        #  P(H|D) = #(observations of D and H) / #(observations of D)
        if len(self.move_list[1])<self.memory:
            return [1.0/3 for i in xrange(3)]

        D = self.move_list[1][-self.memory:]
        N = sum(self.data[D])
        P = [ 1.0*x/N for x in self.data[D] ]
        return P

    def get_move(self):
        if len(self.move_list[0])<self.memory: return random.choice('rps')
        P=self.compute_probabilities()
        #choose a random guess using probabilities.
        x=random.random()
        if x<P[0]: return self.trump( 'r' )
        if x<P[0]+P[1]: return self.trump( 'p' )
        return self.trump( 's' )


#-------------------------------------------------------------------------------

class double_bayes(rps_random):
    """
    Like `bayes`, but also keeps track of its own moves in computing the
    probability distribution.  As a result, tends to not have enough data to
    find patterns in 1000 games if `memory` is greater than 2.
    """
    def __init__(self, memory=1):
        self.move_list=[ '', '' ]
        self.score=[0,0]
        self.moves='rps'
        #memory is the number of moves to keep track of in computing probabilities.
        #Our data requirements for high confidence are exponential in this variable,
        #but should eventually get better predictions with higher memory...
        self.memory=memory
        last=['r', 'p', 's']
        mtuples=last[:]
        #Generate all rps tuples of length memory
        for i in xrange(self.memory-1):
            new=[]
            for a in last: new.append( 'r' + a )
            for a in last: new.append( 'p' + a )
            for a in last: new.append( 's' + a )
            last=new
        self.mtuples=last

        #Observed mtuples of opponent moves, initialized at one observation each.
        keys=[]
        for a in self.mtuples:
            for b in self.mtuples:
                keys.append( (a,b) )
        self.data={ (a,b): [1,1,1] for (a,b) in keys }

    def name(self):
        return 'Double Bayes '+str(self.memory)

    def report(self, my_move, opponent_move, outcome):
        self.move_list[0]+=my_move
        self.move_list[1]+=opponent_move
        i=('rps').index(opponent_move)

        if outcome==1:
            self.score[0]+=1
        elif outcome==-1:
            self.score[1]+=1

        #Update data tables.
        if len(self.move_list[0])>self.memory:
            #m is the previous move
            a = self.move_list[0][-self.memory-1:-1]
            b = self.move_list[1][-self.memory-1:-1]
            new_data=(a,b)
            j='rps'.index( opponent_move )
            self.data[new_data][j]+=1

        if outcome==1:
            self.score[0]+=1
        elif outcome==-1:
            self.score[1]+=1

    def compute_probabilities(self):
        #Using Bayes' theorem, we get that:
        #  P(H|D) = #(observations of D and H) / #(observations of D)
        if len(self.move_list[1])<self.memory:
            return [1.0/3 for i in xrange(3)]

        a = self.move_list[0][-self.memory:]
        b = self.move_list[1][-self.memory:]
        D=(a,b)
        N = sum(self.data[D])
        P = [ 1.0*x/N for x in self.data[D] ]
        return P

    def get_move(self):
        if len(self.move_list[0])<self.memory: return random.choice('rps')
        P=self.compute_probabilities()
        #choose a random guess using probabilities.
        x=random.random()
        if x<P[0]: return self.trump( 'r' )
        if x<P[0]+P[1]: return self.trump( 'p' )
        return self.trump( 's' )

#-------------------------------------------------------------------------------

class max_freq_bayes(bayes):
    """
    Like `bayes`, but always plays to beat the play with highest probability
    given the current game state.  Thus, named the Frequentist.
    """

    def name(self):
        return 'Frequentist '+str(self.memory)

    def get_move(self):
        if len(self.move_list[0])<self.memory: return random.choice('rps')
        P=self.compute_probabilities()
        #return most likely guess.
        return self.trump( 'rps'[P.index(max(P))] )

#-------------------------------------------------------------------------------

class naive_bayes(rps_random):
    """
    Keeps track of number of times H is played when the ith previous move was J,
    for each i in 1 to a specified k.

    Then applies the naive Bayes algorithm on this data.  The number of pieces
    of information is now only linear in k instead of exponential, but we obtain
    a cruder estimate of the probabilities involved using the Naive Bayes
    approximation.

    In fact, we are losing the time data when we apply naive Bayes, so this ends
    up being a really bad algorithm.
    """
    def __init__(self, memory=1):
        self.rps='rps'
        self.move_list=[ '', '' ]
        self.score=[0,0]
        #memory is the number of moves to keep track of in computing probabilities.
        self.memory=memory
        mtuples=[]
        #Generate all rps tuples of length memory
        for i in xrange(self.memory):
            for a in self.rps: mtuples.append( (i,a) )
        self.mtuples=tuple(mtuples)

        #Observed mtuples of opponent moves, initialized at one observation each.
        self.data={ a: [1,1,1] for a in self.mtuples }

        #Number of observations: should be sum of all data vectors.
        self.N=3*len(self.mtuples)

        #Total number of r,p,s thrown by opponent.
        self.opponent_move_totals=[len(self.mtuples) for i in range(3)]

    def name(self):
        return 'Naive Bayes '+str(self.memory)

    def report(self, my_move, opponent_move, outcome):
        self.move_list[0]+=my_move
        self.move_list[1]+=opponent_move

        if outcome==1:
            self.score[0]+=1
        elif outcome==-1:
            self.score[1]+=1

        #Update data tables.
        x=('rps').index(opponent_move)
        for i in range(min([len(self.move_list[1])-2, self.memory])):
            #update entry for the ith-to-last move.
            move=self.move_list[1][-i-2]
            self.data[(i,move)][x]+=1
            #Increased one more data observation.
        self.N+=1
        self.opponent_move_totals[x]+=1

        if outcome==1:
            self.score[0]+=1
        elif outcome==-1:
            self.score[1]+=1

    def compute_probabilities(self):
        #Using Naive Bayes' theorem, we get that:
        #  P(H|D) = scaling_factor* prod( #(observations of D_i and H) / #(observations of D_i) )
        if len(self.move_list[1])==1:
            return [1.0/3 for i in xrange(3)]

        P=[1,1,1]
        n=len(self.mtuples)
        #We insert some random historical data if we haven't played many games yet.
        #This keeps us flexible while figuring out our strategy.
        if len(self.move_list[1])<self.memory:
            D=''
            diff=self.memory-len(self.move_list[1])
            for i in range(diff): D+=random.choice('rps')
            D+=self.move_list[1][-self.memory+diff:]
        else:
            D = self.move_list[1][-self.memory:]
        for i in xrange(3):
            #prior
            P[i]=self.opponent_move_totals[i]*1.0/self.N
            #product of conditionals.
            for j in range(self.memory):
                d=self.data[ (j, D[-j]) ]
                P[i] *= 1.0*d[i]/self.opponent_move_totals[i]
        #Normalize by probability of data.
        scaling_term=sum(P)
        P=[p/scaling_term for p in P]
        return P

    def get_move(self):
        if len(self.move_list[0])<self.memory: return random.choice('rps')
        P=self.compute_probabilities()
        #return most likely guess.
        return self.trump( 'rps'[P.index(max(P))] )

#-------------------------------------------------------------------------------

z1=(-.5+sqrt(3)/2*1j)
z2=(-.5-sqrt(3)/2*1j)
cd={'r':1, 'p':z1, 's':z2}

class diaconis(rps_random):
    """
    `diaconis` is similar to the bayes bot, but we search for interesting
    factors instead of just using the last few moves.

    Factor search uses representations of C_3^m, and iterates over certain
    substrings of the move list to try to find useful factors for predicting
    the next opponent move.

    `M` determines the maximum length substring to use for the factor search.
    With 1000 rounds of RPS, M should probably be 3 or 4.

    `max_width` determines the maximum width of substrings of the move list
    to search in.  A high max_width reduces the number of examples that the
    algorithm will be able to learn on when the width of a substring is
    high relative to the number of moves that have occurred.
    """
    def __init__(self, M=3, max_width=10):
        self.move_list=[ '', '' ]
        #To simplify computations later, we keep track of the game history in a
        #merged move list, where each pair of entries is one turn of play.
        #Odd entries are self's moves, and even entries are opponent moves.
        self.merged_move_list=''
        self.score=[0,0]
        self.rps='rps'
        self.M=M
        self.max_width=max_width
        self.character_tables=[ self.c3m_character_table(m) for m in range(M+1) ]
        self.factors=self.generate_factors(M,max_width,1)
        self.last_checked_factor=[-1 for i in range(M+1)]
        self.best_factor=None
        self.best_factor_score=0

    def name(self):
        return 'Persi'

    #----------
    #The next chunk of code is set-up for doing our fourier transforms on C_3^m
    #and translating between strings and numbers.
    #----------

    def num_to_tuple(self, n, m=None):
        """
        Take a number and generate a tuple of digits base 3 (in reverse order).
        Specifying `m` pads the end of the tuple with zeroes if the length of
        the tuple is less than `m`.
        """
        
        if n==0:
            L=[0]
        else:
            L=[]
            for k in range(ceil(log(n,3).real)+1):
                L.append( ((n//3**k))%3 )
        while len(L)<m: L.append(0)
        if n==0: return tuple(L)
        while L[-1]==0 and len(L)>m: L.pop()
        return tuple(L)
        #This line works well in sage but not pure python:
        #return tuple([int(x) for x in n.str(3)])

    def tuple_to_num(self, t):
        """
        Given a tuple of base 3 digits in reverse order,
        return the corresponding integer.
        """
        return sum([3**(k)*t[k] for k in range(len(t))])

    def tuple_to_rps(self, t):
        """
        Given a tuple of base 3 digits in reverse order,
        return a string of `r`, `p`, and `s` characters.
        """
        out=''
        for i in t:
            out+='rps'[i]
        return out

    def num_to_rps(self, n, m=None):
        """
        Given a number,
        return a string of `r`, `p`, and `s` characters.
        """
        t=self.num_to_tuple(n,m)
        return self.tuple_to_rps(t)

    def c3m_character_table(self, m):
        """
        Generate the character table for C_{3^m}.  Note that the table contains
        (3^m)^2 entries!

        On my (slow) cpu, m=5 takes .5s, and m=6 takes 5.63s.
        Our class generates the appropriate tables at init time, so you should
        use those whenever possible:
        They are stored in `self.character_tables`
        """
        M=[]
        zeta=[exp(i*2*pi*1j/3) for i in range(3)]
        elm_list=[self.num_to_tuple(i,m) for i in range(3**m)]
        for i in range(3**m):
            #Work with the ith representation.
            t=elm_list[i]
            #t gives the exponents used for each of the m generators.
            row = [ prod([zeta[x[j]]**t[j] for j in range(m)]) for x in elm_list ]
            M.append(tuple(row))
        return np.matrix(M)

    def f_from_string(self, s=None, m=None, gaps=None, target=1):
        """
        Generate a likelihood function on C_3^m from the string s.

        `gaps` is a list of length m-1, indicating the number of characters
        to skip after each letter when generating a substring of size m.
        For example, if m=4 and gaps=[2,0,3], then a resulting string
        will look like 'r..ps...p.r', skipping 2 after the first character, 0
        after the second character, and 3 after the third character.  The final
        entry does nothing, since there's no fifth character in the substring.
        The resulting string is then 'rpspr'.

        `target` determines whether to try to predict my own moves (`0`) or the
        opponent's moves (`1`).
        """
        f={}

        if s==None: s=self.merged_move_list
        if m==None: m=self.M
        nmoves=len(s)/2
        if gaps==None: gaps=[0 for i in range(m-1)]
        gaps=list(gaps)
        while len(gaps)>m: gaps.pop()
        #width is the total width of the substrings as they sit in `s`.
        #For example, the substring 'r..ps...p.r' has width 11.
        width=m+sum(gaps)

        #Width determines the number of samples we can take:
        total_samples=len(s)-width

        #We will take slices of `s` and use a set of local indices on the slices.
        local_indices=[gaps[0]]
        gaps=gaps[1:]
        for i in gaps: local_indices.append(local_indices[-1]+i+1)

        #Track the total number of r,p,s, assuming we've seen every possible
        #combination of data and outcome once prior to the start of the game.
        rps_totals=[3**m,3**m,3**m]

        for i in range(nmoves-width-2):
            local=s[2*i:2*i+width]
            w=''
            for j in local_indices: w+=local[j]
            key=w[:]
            out=i+int(math.ceil(width/2))
            if target==1:
                output=s[2*out+1]
            else:
                output=s[2*out]

            q='rps'.index(output)
            rps_totals[q]+=1
            if key in f.keys():
                f[key][q]+=1
            else:
                f[key]=[1,1,1]
                f[key][q]+=1

        #Now create a matrix of probabilities from f..
        g={}
        output=[]
        for i in range(3**m):
            s=self.num_to_rps(i,m)
            if f.has_key(s):
                t=sum(f[s])
                output.append([1.0*x/t for x in f[s]])
            else:
                output.append([1.0/3 for x in range(3)])
        output=np.matrix(output)
        return (f,output)


    def fhat(self, M, absolute=False):
        """
        Generate the Fourier coefficients for a matrix M generated by the
        `f_from_string` method.

        f a function on C_3^m, given as a complex vector of lenth 3^m.  The
        Fourier transform is just the product of the character table time f.
        """
        #m=ceil(log(f.size, 3).real)
        fhat=(self.character_tables[1]*M.transpose()).transpose()
        if absolute:
            sq=lambda a: (a*a.conjugate()).real
            sqv=np.vectorize(sq)
            return sqv(fhat)
        return fhat

    #---------
    # And now we place code for actual in-play factor selection and move generation.
    #---------

    def evaluate_factor(self, m, gaps, target=1):
        """
        Evaluate the viability of a factor.
        
        The factor consists of:
        `m`: The number of moves involved in the factor
        `gaps`: List of size of gaps between the `m` moves
        `target`: 0 for predicting own move, 1 for predicting the opponent's move.

        Returns an estimated distance of the distribution of the factor from
        the uniform distribution.
        """
        (f,M)=self.f_from_string(self.merged_move_list, m=m, gaps=gaps, target=target)
        fhat=self.fhat(M,absolute=True)
        #Creates a 3-tuple which estimates variation distance from the uniform distribution.
        nonuniformity=[sqrt(.25*(x.sum()-1)).real for x in fhat]
        return nonuniformity

    def entropy_of_factor(self, m, gaps, target=1):
        """
        Evaluate the viability of a factor by finding the information entropy in
        the factor.
        
        The factor consists of:
        `m`: The number of moves involved in the factor
        `gaps`: List of size of gaps between the `m` moves
        `target`: 0 for predicting own move, 1 for predicting the opponent's move.
        """
        H=lambda a: a*log(a,2)
        H=np.vectorize(H)
        (f,M)=d.f_from_string(self.merged_move_list, m=m, gaps=gaps, target=target)
        return [-sum(H(x)).real for x in M]

    def generate_factors(self, max_length=4, max_width=10, target=1):
        """
        Generate a list of all possible factors with m<=M and maximum width equal
        to `self.max_width`.
        """
        built={0: []}
        M=max_length
        for m in range(1, M+1):
            built[m]=[]
            #Build all possible sets of gaps.
            #This is the set of weak compositions of l:=max_width-m with m-1 parts.
            l=max_width-m
            curr=[0 for i in range(m+1)]
            curr[-1]=l
            while curr[0]<l:
                #Find next weak composition.
                #Get left-most non-zero entry.
                for i in range(len(curr)):
                    if curr[i]>0: break
                if i>0:
                    curr[i]-=1
                    curr[i-1]+=1
                else:
                    #find the next left-most zero entry.
                    n=curr[i]
                    curr[i]=0
                    for j in range(len(curr)):
                        if curr[j]>0: break
                    curr[j-1]=n+1
                    curr[j]-=1
                built[m].append(curr[:-1])
        return built

    def factor_search(self, target=1):
        best={}
        for m in self.factors.keys():
            max_dist=0
            best_m=None
            gaps=None
            for gaps in self.factors[m]:
                (f,M)=self.f_from_string(self.merged_move_list, m=m, gaps=gaps, target=target)
                fhat=self.fhat(M,m=m,absolute=True)
                #Creates a 3-tuple which estimates variation distance from the uniform distribution.
                U=[sqrt(.25*(x.sum()-1)).real for x in fhat.transpose()]
                d=sum(U)/3
                if d>max_dist:
                    max_dist=d
                    best_m=gaps
                    best_f=f
            if best_m==None:
                best[m]=(None,None)
            else:
                best[m]=(best_m[:], max_dist, f)
        return best

    #-----------
    # Move and report methods.
    #-----------

    def report(self, my_move, opponent_move, outcome):
        self.move_list[0]+=my_move
        self.move_list[1]+=opponent_move
        self.merged_move_list+=my_move
        self.merged_move_list+=opponent_move
        if outcome==1:
            self.score[0]+=1
        elif outcome==-1:
            self.score[1]+=1
        #Evaluate a factor at each number of moves.
        for m in range(1,self.M+1):
            N=len(self.factors[m])
            j=(self.last_checked_factor[m]+1)%N
            score=sum( self.evaluate_factor(m, self.factors[m][j]) )/(3**m)
            if score>self.best_factor_score:
                self.best_factor_score=score
                self.best_factor=(m, self.factors[m][j])
                print self.best_factor, score

    def get_move(self):
        if self.best_factor==None: return random.choice('rps')
        #Use the best factor to generate a move.
        (m,g)=self.best_factor
        f=self.f_from_string(self.merged_move_list, m, g)[0]
        hist=self.merged_move_list[-2*m:]
        local_indices=[g[0]]
        g=g[1:]
        for i in g: local_indices.append(local_indices[-1]+i+1)
        w=''
        for i in local_indices: w+=hist[i]
        if w in f.keys():
            distro=f[w]
            x=random.random()
            i=0
            s=0.0
            while x>s and i<3:
                s+=1.0*distro[i]/sum(distro)
                i+=1
            return 'rps'[(i)%3]
        else:
            return random.choice('rps')

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
def tournament(game_length=1001, games_per_pair=3):
    #Player stable format:
    # (class of player, list of options for initializing class, score=0)
    player_stable = [
        [bayes,[1],0],
        [bayes,[2],0],
        [bayes,[3],0],
        [bayes,[4],0],
        [bayes,[5],0],
        [bayes,[6],0],
        [max_freq_bayes, [3], 0],
        [max_freq_bayes, [4], 0],
        [humanbot,[],0],
        [terminator,[],0],
        [rfind,[],0],
        [naive_bayes,[1],0],
        [naive_bayes,[20],0],
        [random_bias, [],0],
        [freqbot,[],0],
        [switchbot,[],0],
        [beat_last,[],0],
        [rock_622,[],0],
        [reverse_beat_last,[],0],
        [rps_random,[],0],
        [all_rock,[],0],
        [all_scissors,[],0],
        [all_paper,[],0],
        ]
    n=len(player_stable)
    M=[ [0 for i in range(n)] for j in range(n) ]
    for i in range(n):
        for j in range(i+1,n):
            for k in range(games_per_pair):
                a=player_stable[i]
                A=a[0](*a[1])
                b=player_stable[j]
                B=b[0](*b[1])
                G=game_master( A, B, ngames=game_length, early_end=True )
                s=G.run_game()
                if s[0]>s[1]:
                    player_stable[i][2]+=1
                    M[i][j]+=1
                elif s[1]>s[0]:
                    player_stable[j][2]+=1
                    M[j][i]+=1

    #Reporting.
    print 'Number of players: ', n
    print 'Games per player: ', (n-1)*games_per_pair
    scoreboard=player_stable[:]
    scoreboard.sort(key = lambda p: p[2], reverse=True)
    mu=1.0*sum([p[2] for p in scoreboard])/n
    sdev=math.sqrt( sum([ (p[2]-mu)**2 for p in scoreboard ])/(n+1) )
    print 'Average number of games won: ', round( mu, 1 )
    print 'Sdev of games won: ', round( sdev, 1 )

    for p in scoreboard:
        print p[2], '\t|  ',p[0](*p[1]).name()
    return M

def faceoff(A,B, ngames=20, nrounds=1000):
    A=[A[0], A[1], 0]
    B=[B[0], B[1], 0]
    wins=[0,0]
    for i in range(ngames):
        A0=A[0](*A[1])
        B0=B[0](*B[1])
        G=game_master(A0, B0, nrounds, False)
        G.run_game()
        if G.score[0]>G.score[1]:
            wins[0]+=1
        elif G.score[0]<G.score[1]:
            wins[1]+=1
    return wins


