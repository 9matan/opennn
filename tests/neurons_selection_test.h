//   OpenNN: Open Neural Networks Library
//   www.opennn.net
//
//   N E U R O N S   S E L E C T I O N   T E S T   C L A S S   H E A D E R
//
//   Artificial Intelligence Techniques SL
//   artelnics@artelnics.com                                           

#ifndef NEURONSSELECTIONALGORITHMTEST_H
#define NEURONSSELECTIONALGORITHMTEST_H

// Unit testing includes

#include "unit_testing.h"

class NeuronsSelectionTest : public UnitTesting
{

public:

   // CONSTRUCTOR

   explicit NeuronsSelectionTest();

   virtual ~NeuronsSelectionTest();

   // Constructor and destructor methods

   void test_constructor();
   void test_destructor();

   // Get methods

   void test_get_training_strategy_pointer();

   void test_get_loss_calculation_method();

   void test_write_loss_calculation_method();

   // Set methods

   void test_set_training_strategy_pointer();


   // Unit testing methods

   void run_test_case();

private:

   DataSet data_set;

   NeuralNetwork neural_network;

   TrainingStrategy training_strategy;

};


#endif
