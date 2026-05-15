class Node {
    public:
        int key; int val; Node* prev; Node* next;
        Node(int k, int v) {
            key = k;
            val = v;
            prev = nullptr;
            next = nullptr;
        }
};

class LRUCache {
    private:
        Node* add (int k, int v) {
            Node* n = new Node(k,v);
            n->prev = left->prev;
            left->prev->next = n;
            left->prev = n;
            n->next = left;
            return n;
        }

        void remove (Node* n) {
            Node* t = n->next;
            t->prev = n->prev;
            n->prev->next = t;
        }

    public:
        int cap;
        int c;
        Node* left; Node* right;
        unordered_map<int, Node*> dic;
        LRUCache(int capacity) {
            cap = capacity;
            dic = {};
            c = 0;
            left = new Node(0,0);
            right = new Node(0,0);
            left->prev = right;
            right->next = left;
        }
        
        int get(int key) {
            if (dic.count(key) != 1) 
                return -1;
            remove(dic[key]);
            dic[key] = add(dic[key]->key, dic[key]->val);
            return dic[key]->val;
        }
        
        void put(int key, int value) {
            if (dic.count(key) == 1) {
                dic[key]->val = value;
                remove(dic[key]);
                dic[key] = add(dic[key]->key, dic[key]->val);
            } else {
                dic[key] = add(key,value);
                c++;
                if (c > cap) {
                    c--;
                    dic.erase(right->next->key); 
                    remove(right->next);
                }
            }

        }
};
