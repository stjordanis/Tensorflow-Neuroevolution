import tensorflow as tf
from absl import logging

import neuroevolution as ne


def main():
    """
    A simple example used in the current alpha stage of development to show of the Tensorflow-Neuroevolution framework.
    This example uses the NEAT ne-algorithm with a direct encoded genome to solve the basic XOR environment.

    :return: None
    """
    logging.set_verbosity(logging.DEBUG)
    logging.info("Using TF Version {}".format(tf.__version__))
    assert tf.__version__[0] == '2'  # Assert that TF 2.x is used

    config = ne.load_config('./xor_neat_example.cfg')

    environment = ne.environments.XOREnvironment()

    encoding = ne.encodings.DirectEncoding(config, dtype=tf.float32, run_eagerly=False)
    ne_algorithm = ne.algorithms.NEAT(encoding, config)

    population = ne.Population(ne_algorithm, config)

    engine = ne.EvolutionEngine(population, environment)

    best_genome = engine.train()

    if best_genome is not None:
        environment.replay_genome(best_genome)
        logging.info("Best Genome returned by evolution:\n{}".format(best_genome))
        logging.info("Visualizing best genome returned by evolution...")
        best_genome.visualize()
    else:
        logging.info("Evolution of population did not return a valid genome")


if __name__ == '__main__':
    main()
