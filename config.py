import warnings


class DefaultConfig(object):
    # visdom environment
    env = 'AI_final_project'
    # choose model , in accord with model/__init__.py
    model = 'ResNet34'
    
    # train set path
    train_data_root = './data/train'
    # test set path
    test_data_root = './data/test'
    # model path
    load_model_path = f'checkpoints/{model}.pth'

    batch_size = 128 # batch size
    device = 'cup'   # GPU or CPU
    num_workers = 1  # how many workers for loading data
    print_freq = 20  # print info every N batch

    debug_file = '/tmp/debug' # if os.path.exists(debug_file): enter ipdb
    result_file = 'result.csv'
      
    max_epoch = 20
    lr = 0.1            # initial learning rate
    lr_decay = 0.95     # when val_loss increase, lr = lr*lr_decay
    weight_decay = 1e-4 # loss



def parse(self,kwargs):
        '''
        update parameter according to key
        '''
        for k,v in kwargs.iteritems():
            if not hasattr(self,k):
                warnings.warn("Warning: opt has not attribut %s" %k)
            setattr(self,k,v)

        print('user config:')
        for k,v in self.__class__.__dict__.iteritems():
            if not k.startswith('__'):
                print(k,getattr(self,k))


DefaultConfig.parse = parse
opt = DefaultConfig()