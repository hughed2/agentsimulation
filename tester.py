"""
   Tester file for the agent code

"""

import simulation as sim
import simplejson as sj
import random
import sys
import simulation as sim

def print_results(results):
    print "Trust: %r, Filter: %r, Inbox: %r\n SA: %s\t Comm: %s\t Steps %s" \
        %(results['setup']['trust_used'], \
          results['setup']['trust_filter_on'], \
          results['setup']['inbox_trust_sorted'], \
          results['summary_results']['sa'], \
          results['summary_results']['comm'], \
          results['summary_results']['steps'])
    for val in results['summary_results']['sa_at_value']:
        print "Steps: %d\t Comm:%.1f\t @sa %.1f" \
            %(val['steps'],val['comm'],val['sa'])

    print "Total filtered", results['total_filtered']

if __name__ == '__main__':
    num_steps = 10000
    num_trial = 20
    num_facts = 50
    num_noise = 5000
    num_agents = 20
    agent_per_fact = 1
    connection_probability = 1
    willingness = 1
    competence = 1
    graph_type = 'collaborative'
    #graph_type = 'spatial_random'
    #graph_type = 'hierarchy'
    spamminess = 0
    selfishness = 0
    agent_setup = []

    trust_used = False
    inbox_trust_sorted = False
    trust_filter_on = False

    #for (trust_used, trust_filter_on, inbox_trust_sorted) in \
    #    [(False,False,False), (True, True, False), (True, True, True)]:
    for (trust_used, trust_filter_on, inbox_trust_sorted) in \
        [(False,False,False)]:
        
        results = sim.run_simulation(NUM_FACTS=num_facts, \
                                     NUM_NOISE=num_noise, \
                                     NUM_AGENTS=num_agents, \
                                     AGENT_PER_FACT=agent_per_fact, \
                                     CONNECTION_PROBABILITY=connection_probability, \
                                     NUM_STEPS=num_steps, \
                                     WILLINGNESS=willingness, \
                                     COMPETENCE=competence, \
                                     NUM_TRIAL=num_trial,\
                                     GRAPH_TYPE=graph_type, \
                                     AGENT_SETUP=agent_setup, \
                                     SPAMMINESS=spamminess, \
                                     SELFISHNESS=selfishness, \
                                     TRUST_USED=trust_used, \
                                     INBOX_TRUST_SORTED=inbox_trust_sorted,\
                                     TRUST_FILTER_ON=trust_filter_on)
        
        print_results(results)