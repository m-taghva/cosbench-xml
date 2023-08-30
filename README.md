# cosbench-xml
scripts for generating xml configuration file in cosbench a bench marking tool for testing swift object storage.

      (customize-xml.py) this script can generate many xml configuration with uniq name and different config.
      use: # python3 customize-xml.py
      output: swift_config_sample_(n).xml
      ===========================================
      (xmlgen.py) in workload-gen directory just edit worker number in main work stage.
      you can send your maximum worker number to script and it can generate new xml file. it can count double until maximum. 
      use: # python3 xmlgen.py 
          Enter the XML file name: 
          Enter the maximum number of workers: 
      ===========================================
