# - Author: Soheil Esmaeilzadeh
# - Created on: 08/08/2021
# - Email: soes@alumni.stanford.edu

# - Problem Description:
# -- Given a function that simulates tossing a fair coin with equal probabilities of getting tail (0) or head (1), 
# -- write a function that simulates an unfair coin toss where its probability of getting heads (1) is 'p' 

# ---------------------------------------------------- #

import os
import random
import matplotlib.pyplot as plt
import logging
random.seed(31)

# ---------------------------------------------------- #

def fair_coin_single_toss():

    '''
    A function for simulating a single toss of a fair coin (i.e., equal head/tail probabilities)
    Parameters
    ----------
    None

    Returns
    -------
    fair_coin_single_toss_outcome: int
        a randomly generated integer with an equally probable value of 0 or 1 corresponding to tail or head outcomes
    '''

    fair_coin_single_toss_outcome = random.randint(0,1)
    
    return fair_coin_single_toss_outcome

# ---------------------------------------------------- #

def fair_coin_toss_sequence(n=3):

    '''
    A function for simulating tossing a sequence of fair coins
    Parameters
    ----------
    n: int
        number of times a fair coin is tossed

    Returns
    -------
    toss_sequence: string
        a string of '1's and '0' for the times the fair coin comes out head or tail
        e.g., a sequence of 3 as 'head'-'tail'-'head' would be '101'
    '''

    fair_coin_toss_sequence_outcome = "".join([str(fair_coin_single_toss()) for i in range(n)])

    return fair_coin_toss_sequence_outcome

# ---------------------------------------------------- #

def unfair_coin(s0, s1):

    '''
    A function for simulating tossing an unfair coin
    Parameters
    ----------
    s0: list[strings]
        fair coin toss sequence outcomes for which we return 0
    s1: list[strings]
        fair coin toss sequence outcomes for which we return 1

    Note:
    ----------
        for fair coin toss sequence outcomes outside of s0 or s1 we redo the 'fair_coin_toss_sequence'

    Returns
    -------
    unfair_coin_outcome: int
        0 for fair coin toss sequence outcomes that are in s0
        1 for fair coin toss sequence outcomes that are in s1
        retry for fair coin toss sequence outcomes that are NOT in s1 or s0
    '''

    while True:

        # get a sequence of fair coin tosses
        num = fair_coin_toss_sequence(n=len(s1[0]))

        # return 1
        if num in s1: 
            unfair_coin_outcome = 1 
            return unfair_coin_outcome

        # return 0
        elif num in s0:
            unfair_coin_outcome = 0 
            return unfair_coin_outcome

        # RE-try
        else:
            continue 
    

# ---------------------------------------------------- #

if __name__ == '__main__':

    # logging
    output_dir    = "./outputs/"
    if  not os.path.exists(output_dir): os.mkdir(output_dir)
    level, format = logging.INFO, '  %(message)s'
    handlers      = [logging.FileHandler(output_dir+'logs.txt', mode='w'), logging.StreamHandler()]
    logging.basicConfig(level=level, format=format, handlers=handlers)

    # ---------------------------------------------------- #

    # Let's aim for a probability of 3/10
    ## number of bits (or sequence of fair coin toss attempts) -> ceil(log2(10)) = 4
    ### -> 3 scenarios out of 10 where we return '1'
    s1 = ["1111","1110","1101"] 
    ### -> 9 scenarios out of 10 where we return '0'
    s0 = ["1011","0111","1100","1001","0011","1000","0001"] # 9 scenarios where we return '0'

    target_prob = round(len(s1)/(len(s0)+len(s1)),3)
    logging.info("===== ***** Simulation of an unfair coin ***** =====", target_prob)
    logging.info("The target probability is:", target_prob)

    # ---------------------------------------------------- #

    n_iters = [2**i for i in range(15)]
    outcome_prob, err = [], []

    for n_iter in n_iters:

        logging.info("-"*100)
        logging.info("After {} number of trials: ".format(n_iter))

        simulation_prob = round(sum([unfair_coin(s0, s1) for i in range(n_iter)])/n_iter,3)
        error           = round(abs(target_prob-simulation_prob),3)
        outcome_prob.append(simulation_prob)
        err.append(error)

        logging.info("-> the calculated probability of the biased coin is {}, and the expected probability error is: {}".format(simulation_prob, error))
        logging.info("-"*100)
    
    # ---------------------------------------------------- #

    plot_prob, plot_err = True, True
    plt.figure(figsize=[7*sum([int(plot_prob),int(plot_err)]),6])
    print(7*sum([int(plot_prob),int(plot_err)]))
    
    if plot_prob:
        if plot_err: plt.subplot(1,2,1)
        plt.plot(n_iters,outcome_prob, color='blue', marker='o', linestyle='dashed', linewidth=1, markersize=5, alpha=1)
        plt.plot(n_iters, [0.3]*len(n_iters), color='black', linestyle='dashdot', linewidth=1, markersize=5)

        plt.ylim([-0.1,1.1]) 
        plt.xscale('log', basex=2)

        plt.xlabel("Number of Coin Tosses", fontsize=14)
        plt.ylabel("P(Head)", fontsize=14)
        
        plt.xticks([2**n for n in range(0,len(err)+1,2)], [f"$2^{ {n} }$" for n in range(0,len(err)+1,2)]) 
        plt.yticks([0,0.3,0.5,1]) 

        plt.title("(a) Unfair Coin Simulation with a Head Probability of 0.3")
        plt.legend(["simulation probability", "target probability"])

    if plot_err:
        if plot_prob: plt.subplot(1,2,2)
        plt.bar(range(len(err)), err, color='r',alpha=1)

        plt.ylim([0.001,1]);
        plt.yscale('log', basey=10)

        plt.xlabel("Number of Coin Tosses", fontsize=14)
        plt.ylabel("Error = |P(Head) - 0.3|", fontsize=14)
        
        plt.xticks(range(0,len(err)+1,2), [f"$2^{ {n} }$" for n in range(0,len(err)+1,2)]) 
        plt.yticks([10**(-n) for n in range(4)])
        
        plt.title("(b) Unfair Coin Simulation with a Head Probability of 0.3")
        plt.legend(["Error Bars"])
    
    plt.savefig(output_dir + "simulation-results.png")
