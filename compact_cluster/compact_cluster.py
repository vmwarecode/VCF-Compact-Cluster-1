#Compact cluster
#Removes a host from a cluster
import sys
import os
sys.path.append(os.path.abspath(__file__ + '/../../'))
from Utils.utils import Utils
import pprint

class CompactCluster:
    def __init__(self):
        print('Compact Cluster')
        self.utils = Utils(sys.argv)
        self.hostname = sys.argv[1]
        self.cluster_id = sys.argv[4]

    def compact_cluster(self):
        data = self.utils.read_input(os.path.abspath(__file__ +'/../')+'/compact_cluster_spec.json')
        validations_url =  'https://'+self.hostname+'/v1/clusters/'+self.cluster_id+'/validations/updates'
        print ('Validating the input....')
        response = self.utils.post_request(data,validations_url)
        if(response['resultStatus'] != 'SUCCEEDED'):
            print ('Validation Failed.')
            exit(1)

        compact_cluster_url = 'https://'+self.hostname+'/v1/clusters/'+self.cluster_id
        response = self.utils.patch_request(data,compact_cluster_url)
        tasks_url = 'https://'+self.hostname+'/v1/tasks/' + response['id']
        print('Compact Cluster finished with status: ' + self.utils.poll_on_id(tasks_url,True))


if __name__== "__main__":
    CompactCluster().compact_cluster()
