
class trainersNetwork:
  def __init__(self):
    self.trainerSubjects=[]
    self.edges=[[0]]
  #To add vertices to the graph
  def add_vertex(self,v):
    global vertices_no,output
    if v in self.trainerSubjects:
      return
    else:
      vertices_no=vertices_no+1
      self.trainerSubjects.append(v)
      if vertices_no>1:
        for edge in self.edges:
          edge.append(0)
        temp=[]
        for i in range(vertices_no):
          temp.append(0)
        self.edges.append(temp)
    return 
  #To add edges to the graph
  def add_edges(self,v1,v2):
    #print(v1,v2)
    if v1 not in self.trainerSubjects:
      print(v1,' not in the graph structure')
    elif v2 not in self.trainerSubjects:
      print(v2,' not in the graph structure')
    else:
      index1=self.trainerSubjects.index(v1)
      #print(index1)
      index2=self.trainerSubjects.index(v2)
      #print(index2)
      self.edges[index1][index2]=1
      #self.edges[index2][index2]=1

  def readInput(self, inputfile):
    Lines = input_file.readlines()
    data=[]
    for line in Lines:
      temp=[]
      t=[]
      for j in line:
        if j.isalpha():
          t.append(j)
        elif j=='/':
          t1=[]
          t1=t
          t=[]
          text=''.join(t1)
          temp.append(text)
      temp.append(''.join(t))
      data.append(temp)
    self.graph_loading(data)
    #print(self.trainerSubjects)
    #print(np.array(self.edges))
    return 
  
  def showAll(self):
    log_out('\n--------Function showAll--------\n')
    trainers=[]
    subjects=[]
    for i in range(len(self.edges)):
      sum=0
      for j in range(len(self.edges)):
         sum=sum+self.edges[i][j]
      if sum>0:
        trainers.append(self.trainerSubjects[i])
      else:
        subjects.append(self.trainerSubjects[i])
    log_out(log='Total No. of trainers: '+str(len(trainers))+'\n')
    log_out(log='Total No. of subjects: '+str(len(subjects))+'\n')
    log_out('\nList of Trainers: \n')
    for i in trainers:
      log_out(log=i+'\n')
    log_out('\nList of Subjects: \n')
    for i in subjects:
      log_out(log=i+'\n')
    return log_out('-----------------------------------------\n')

  def itero(self):
    idx=[]
    for i in range(len(self.edges)):
      count=0
      for j in range(len(self.edges)):
        sum=0
        for k in range(len(self.edges)):
          if i!=k:
          #self.edges[i][count]!=self.edges[j][k]:
            sum=sum+self.edges[k][j]
          else:
            continue  
        #print(self.edges[i][count])
        #print(i,count,sum)
        if self.edges[i][count]>sum:
          idx.append(i)
        elif self.edges[i][count]==1 and sum==1:
          idx.append(i)
        else:
          pass
        count=count+1
    #print(idx)
    out=[]
    for ids in idx:
      if ids not in out:
        out.append(ids)
    return out

  def displayRecruitList(self):
    log_out('\n--------Function displayRecruitList --------\n')
    index=self.itero()
    #print(index)
    log_out(log='No of trainers required to cover all subjects: '+str(len(index))+'\n')
    for ids in index:
      log_out(log=self.trainerSubjects[ids])
      for j in range(len(self.edges)):
        if self.edges[ids][j]==1:
          log_out(log=' / '+self.trainerSubjects[j])
      log_out('\n')
    return log_out('-----------------------------------------\n')


  def displayTrainers(self, subj): 
    log_out('\n--------Function displayTrainers --------\n')
    pos=[]
    for i,item in enumerate(self.trainerSubjects):
      if item==subj:
        pos.append(i)
    log_out(log='List of trainers who can teach '+subj+':\n')
    for i in pos:
      #print(i)
      for j in range(len(self.edges)):
        #print(j)
        if self.edges[j][i]==1:
         if i!=j:
           log_out(log=self.trainerSubjects[j]+'\n')
         else:
           continue
    return log_out('-----------------------------------------\n')


  def graph_loading(self,dataset):
    #print(dataset)
    #adding each trainer and subjects into the list
    for i,items in enumerate(dataset):
      for j,data in enumerate(items):
        self.add_vertex(data)
    #print(dataset)
    #setting the edges between each trainers and subjects
    for i,items in enumerate(dataset):
      trainer=items[0]
      #print(items[0])
      for j in range(1,len(items)):
        self.add_edges(trainer,items[j])

def log_out(log):
  output.write(log)

def extracting_prompts():
  prompt_file=open('promptsPS13.txt','r')
  lines=prompt_file.readlines()
  prompts=[]
  for line in lines:
      temp=[]
      t=[]
      counter=0
      for j in line:
        if j.isalpha():
          t.append(j)
        elif j==':':
          counter=1
          t1=[]
          t1=t
          t=[]
          text=''.join(t1)
      if counter:
        prompts.append((text,''.join(t)))
      else:
        prompts.append((''.join(t),''))
  return prompts

def reading_prompts(prompt_file):
  for i,items in enumerate(prompt_file):
    if items[1]!='':
      if items[0]=='findSubject':
       trainers.displayTrainers(items[1])
      else:
        log_out(items[0])
        log_out('Invalid Operation')
    else:
      if items[0]=='showMinList':
        trainers.displayRecruitList()
      else: 
        log_out(items[0])
        log_out('Invalid Operation')
  return 

if __name__ == '__main__':
  import numpy as np
  global output,trainers
  vertices_no=0
  output=open('outputPS13.txt','w')
  input_file=open('inputPS13.txt','r')
  trainers=trainersNetwork()
  trainers.readInput(input_file)
  trainers.showAll()
  prompts=extracting_prompts()
  reading_prompts(prompts)
  