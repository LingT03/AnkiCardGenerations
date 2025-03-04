# To run this script:
# 1. Install genanki if not installed: pip install genanki
# 2. Run this python script: python generate_anki_cards.py
# 3. It will produce a file named "CloudComputingFlashcards.apkg".
# 4. Import the resulting .apkg file into Anki.

import genanki

# We'll define a custom model for multiple-choice cards.
my_model = genanki.Model(
    1607392319,  # A random model ID
    'Cloud MCQ Model',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'}
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Question}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
        },
    ]
)

# We'll define a list of (question, choices, answer) tuples.
qa_data = [
    # QUIZ 1
    ("Which of the following is a key benefit of cloud computing to allow companies to reduce their upfront investment in data centers and equipment?",\
     "1. Increased capital expenses\n2. Enhanced security protocols\n3. Trade capital expenses for operating expenses\n4. Improved software development lifecycle",\
     "Trade capital expenses for operating expenses"),
    ("Which of the following best describes the concept of Total Cost of Ownership (TCO) in cloud computing?",\
     "1. The initial purchase price of cloud services\n2. The direct and indirect costs of a product or service over its entire lifecycle\n3. The operational costs of maintaining on-premises data centers\n4. The cost savings achieved by using cloud computing",\
     "The direct and indirect costs of a product or service over its entire lifecycle"),
    ("Which of the following best describes the concept of economy of scale in the context of cloud computing?",\
     "1. The advantage gained by companies from expanding their scale of operations, leading to cost efficiencies\n2. The ability to reduce the number of employees needed to manage IT infrastructure\n3. The process of automating application deployment in the cloud\n4. The method of encrypting data at rest and in transit",\
     "The advantage gained by companies from expanding their scale of operations, leading to cost efficiencies"),
    ("Which architecture structures an application as a collection of small, highly specialized services, each responsible for a specific functionality?",\
     "1. Service-Oriented Architecture (SOA)\n2. Monolithic Architecture\n3. Microservices Architecture\n4. Client-Server Architecture",\
     "Microservices Architecture"),
    ("Which method allows companies to deploy applications in the cloud using code to define infrastructure?",\
     "1. Web Console\n2. Command-Line Interface (CLI)\n3. Software Development Kit (SDK)\n4. Infrastructure Configuration Language (HCL)",\
     "Infrastructure Configuration Language (HCL)"),
    ("Which of the following cloud computing models provides the highest level of abstraction, allowing users to access software applications over the internet without managing the underlying infrastructure?",\
     "1. Infrastructure as a Service (IaaS)\n2. Platform as a Service (PaaS)\n3. Software as a Service (SaaS)\n4. Function as a Service (FaaS)",\
     "Software as a Service (SaaS)"),
    ("Which of the following is a method for deploying applications in the cloud using a graphical user interface?",\
     "1. Command-Line Interface (CLI)\n2. Web Console\n3. Infrastructure Configuration Language (HCL)\n4. Software Development Kit (SDK)",\
     "Web Console"),
    ("Which of the following is a key motivation for businesses to adopt cloud computing?",\
     "1. Increased capital expenses\n2. Limited scalability\n3. Pay-as-you-go pricing model\n4. Reduced flexibility",\
     "Pay-as-you-go pricing model"),
    ("Which of the following best describes the benefit of cloud computing in terms of scalability?",\
     "1. Fixed capacity based on initial setup\n2. Limited to scaling only during peak hours\n3. Requires manual intervention for scaling\n4. Ability to scale capacity up and down based on demand",\
     "Ability to scale capacity up and down based on demand"),
    ("Which of the following describes the ability of cloud computing to align costs with actual usage?",\
     "1. Pay-as-you-go pricing model\n2. Fixed pricing model\n3. Subscription-based pricing model\n4. Upfront capital investment",\
     "Pay-as-you-go pricing model"),

    # QUIZ 2
    ("What is the primary purpose of the Internet Layer in the TCP/IP architecture?",\
     "1. To provide end-to-end communication between applications using port numbers.\n2. To define the format and order of messages exchanged between communication entities\n3. To allow intercommunication between hosts on distinct physical networks.\n4. To translate domain names to IP addresses.",\
     "To allow intercommunication between hosts on distinct physical networks."),
    ("What is the main advantage of using a layered architecture in computer networks?",\
     "1. It allows for the use of different transmission media.\n2. It simplifies interoperability and promotes the reuse of components.\n3. It ensures that all layers are implemented by the same manufacturer.\n4. It provides a single, seamless communication system.",\
     "It simplifies interoperability and promotes the reuse of components."),
    ("What is the purpose of subnetting in the context of IPv4 addresses?",\
     "1. To allow a more efficient use of the allocated range of IP addresses in a network.\n2. To increase the number of available IP addresses.\n3. To translate domain names to IP addresses.\n4. To translate an IP to MAC address",\
     "To allow a more efficient use of the allocated range of IP addresses in a network."),
    ("Which of the following is a characteristic of the Transmission Control Protocol (TCP)?",\
     "1. It does not guarantee the delivery of data packets.\n2. It uses MAC addresses to identify applications.\n3. It does not require the establishment of a connection between sender and receiver.\n4. It provides a connection-oriented service with guaranteed delivery and sequencing.",\
     "It provides a connection-oriented service with guaranteed delivery and sequencing."),
    ("What is the main goal of the Domain Name System (DNS)?",\
     "1. To translate IP addresses to MAC addresses.\n2. To allow two physical networks to communicate with each other.\n3. To translate domain names to IP addresses.\n4. To provide end-to-end communication between applications.",\
     "To translate domain names to IP addresses."),
    ("What is the primary purpose of Network Address Translation (NAT)?",\
     "1. To translate domain names to IP addresses.\n2. To map local (private) IP addresses to a single public IP address.\n3. To assign IP addresses to devices on a network.\n4. To provide end-to-end communication between applications.",\
     "To map local (private) IP addresses to a single public IP address."),
    ("Given an IP network address in CIDR notation of 192.168.10.0/26, how many hosts can be configured within this subnet?",\
     "1. 30\n2. 62\n3. 126\n4. 254",\
     "62"),
    ("Given an IP network address in CIDR notation of 192.168.10.0/26, how many subnets can be configured if we borrow 2 bits for subnetting?",\
     "1. 2\n2. 4\n3. 8\n4. 16",\
     "4"),
    ("Which of the following transport layer protocols uses port numbers to identify applications and provides a connection-oriented service?",\
     "1. UDP\n2. TCP\n3. ICMP\n4. ARP",\
     "TCP"),
    ("Which of the following is a characteristic of the User Datagram Protocol (UDP)?",\
     "1. It guarantees the delivery of data packets\n2. It requires the establishment of a connection between sender and receiver.\n3. It provides a connection-oriented service with sequencing.\n4. It does not guarantee the delivery of data packets and does not require a connection.",\
     "It does not guarantee the delivery of data packets and does not require a connection."),
    ("UDP (User Datagram Protocol) ensures that datagrams are delivered in the correct order.",\
     "1. True\n2. False",\
     "False"),
    ("When a datagram does not fit into a single packet and has to be broken into multiple packets, UDP ensures that all packets will arrive at the destination.",\
     "1. True\n2. False",\
     "False"),

    # QUIZ 3
    ("Which of the following statements about AWS IAM roles is correct?",\
     "1. An IAM role is associated with a specific person and has long-term credentials.\n2. An IAM role can be assumed by users, applications, or services and is not associated with a specific person.\n3. An IAM role is a collection of users that makes it easier to manage permissions for multiple users at once.\n4. An IAM role is a virtual firewall that controls inbound and outbound traffic at the instance level.",\
     "An IAM role can be assumed by users, applications, or services and is not associated with a specific person."),
    ("Which of the following elements is NOT part of an AWS policy statement?",\
     "1. Effect\n2. Action\n3. Resource\n4. Protocol",\
     "Protocol"),
    ("Which of the following is a characteristic of symmetric encryption?",\
     "1. It uses two keys: one public and one private.\n2. It is slower than asymmetric encryption.\n3. It uses the same key for both encryption and decryption.\n4. It is the preferable method for secret exchange",\
     "It uses the same key for both encryption and decryption."),
    ("The 'Version' element in an AWS policy document specifies the date when the policy was created or last updated.",\
     "1. True\n2. False",\
     "False"),
    ("Which of the following is a feature of AWS Security Groups?",\
     "1. They are stateless and require explicit inbound and outbound rules.\n2. They operate at the network level and control traffic to and from subnets.\n3. They are virtual firewalls that control inbound and outbound traffic at the instance level.\n4. They are used to manage permissions across AWS accounts in AWS Organizations.",\
     "They are virtual firewalls that control inbound and outbound traffic at the instance level."),
    ("Which of the following statements correctly describes the difference between a trust policy and a resource-based policy in AWS?",\
     "1. A trust policy defines which entities are allowed to assume an IAM role, while a resource-based policy specifies permissions for actions on a specific resource.\n2. A trust policy specifies permissions for actions on a specific resource, while a resource-based policy defines which entities are allowed to assume an IAM role.\n3. Both trust policies and resource-based policies specify permissions for actions on specific resources.\n4. Both trust policies and resource-based policies define which entities are allowed to assume an IAM role.",\
     "A trust policy defines which entities are allowed to assume an IAM role, while a resource-based policy specifies permissions for actions on a specific resource."),
    ("Which of the following best describes the purpose of a digital certificate?",\
     "1. It is an electronic document used to prove the authenticity of a device, server, or user.\n2. It a service used to manage encryption keys for securing data.\n3. It defines permissions for actions on specific resources.\n4. It controls inbound and outbound traffic at the instance level",\
     "It is an electronic document used to prove the authenticity of a device, server, or user."),
    ("Which of the following best describes the purpose of Multi-Factor Authentication (MFA)?",\
     "1. It is a virtual firewall that controls inbound and outbound traffic at the instance level\n2. It is a service that manages encryption keys for securing data\n3. It is a type of policy used to manage permissions across accounts\n4. It is a mechanism that requires users to provide two or more verification factors to gain access to AWS resources",\
     "It is a mechanism that requires users to provide two or more verification factors to gain access to AWS resources"),
    ("Which of the following best describes the purpose of AWS Identity and Access Management (IAM) policies?",\
     "1. They manage encryption keys used to secure data at rest and in transit\n2. They define which entities are allowed to assume an IAM role\n3. They control inbound and outbound traffic at the instance level.\n4. They specify what actions are allowed or denied for identities or resources",\
     "They specify what actions are allowed or denied for identities or resources"),
    ("Which of the following statements correctly describes the difference between security groups and Access Control Lists (ACLs) in AWS?",\
     "1. Security groups control traffic at the instance level, while ACLs control traffic at the subnet level.\n2. Security groups are stateless and require explicit inbound and outbound rules, while ACLs are stateful and automatically allow responses to traffic\n3. Security groups are used to manage permissions across AWS accounts, while ACLs specify permissions for actions on specific AWS resources\n4. Security groups and ACLs both control traffic at the instance level",\
     "Security groups control traffic at the instance level, while ACLs control traffic at the subnet level."),

    # QUIZ 4
    ("Best definition of virtualization.",\
     "1. The process of creating physical hardware\n2. The creation of a software abstraction layer over computer hardware\n3. The process of removing software from hardware\n4. The creation of physical networks",\
     "The creation of a software abstraction layer over computer hardware"),
    ("Which of the following is NOT considered a type of virtualization?",\
     "1. Network virtualization\n2. Storage virtualization\n3. Server virtualization\n4. Application virtualization",\
     "Application virtualization"),
    ("In AWS, what is a region?",\
     "1. A single data center\n2. A separate geographical area isolated from each other\n3. A type of storage\n4. A virtual machine",\
     "A separate geographical area isolated from each other"),
    ("What is a Virtual Private Cloud (VPC) in AWS?",\
     "1. A physical network\n2. A pool of network resources allocated to customers in a public cloud environment\n3. A type of storage\n4. A type of server",\
     "A pool of network resources allocated to customers in a public cloud environment"),
    ("Which type of hypervisor runs directly on the physical machine hardware?",\
     "1. Type-1\n2. Type-2\n3. Type-3\n4. Type-4",\
     "Type-1"),
    ("What is the main advantage of Type-1 hypervisors over Type-2 hypervisors?",\
     "1. They are cheaper\n2. They are easier to install\n3. They provide better performance and efficiency\n4. They require less hardware",\
     "They provide better performance and efficiency"),
    ("What is Elastic Block Store (EBS) in AWS?",\
     "1. A type of network\n2. A type of block storage\n3. A type of file system storage\n4. A type of object storage",\
     "A type of block storage"),
    ("Which AWS service is used for file storage?",\
     "1. EBS\n2. S3\n3. EFS\n4. EC2",\
     "EFS"),
    ("What is the maximum size of an object that can be stored in AWS S3?",\
     "1. 1TB\n2. 2TB\n3. 5TB\n4. 10TB",\
     "5TB"),
    ("What is the purpose of a NAT (Network Address Translator) in a private subnet in AWS?",\
     "1. To provide direct internet access\n2. To enable communication between instances in different subnets\n3. To allow instances/services in a private subnet to communicate with the internet\n4. To control traffic between subnets",\
     "To allow instances/services in a private subnet to communicate with the internet"),
    ("Why might you choose Amazon S3 for your storage needs?",\
     "1. It operates on top of the network level using protocols like NFS and SMB\n2. It provides block storage with fast, efficient, and reliable data transportation\n3. It stores data as objects and is accessed via transport protocols such as HTTP using REST APIs\n4. It allows for the creation of raw storage volumes ideal for data transportation",\
     "It stores data as objects and is accessed via transport protocols such as HTTP using REST APIs"),
    ("Why might you choose Amazon EFS for your storage needs?",\
     "1. It operates on top of the network level using protocols like NFS and SMB\n2. It provides block storage with fast, efficient, and reliable data transportation\n3. It stores data as objects and is accessed via transport protocols such as HTTP using REST APIs\n4. It allows for the creation of raw storage volumes ideal for data transportation",\
     "It operates on top of the network level using protocols like NFS and SMB"),
    ("Which AWS storage virtualization service allows attaching volumes to multiple simultaneous EC2 instances?",\
     "1. EBS\n2. EFS\n3. S3\n4. ECS",\
     "EFS"),
    ("In Amazon S3, you cannot create actual folder structures, but you can simulate them using naming conventions.",\
     "1. True\n2. False",\
     "True"),
    ("Amazon S3 is the fastest storage virtualization option in AWS.",\
     "1. True\n2. False",\
     "False"),
]


# Create a Deck
deck = genanki.Deck(
    2059400110,  # A random deck ID
    'Cloud Computing MCQs'
)

# Add notes to the deck
for question, choices, answer in qa_data:
    note = genanki.Note(
        model=my_model,
        fields=[f"{question}<br><br>{choices}", answer]
    )
    deck.add_note(note)

# Create a package and write to file
package = genanki.Package(deck)
package.write_to_file('CloudComputingFlashcards.apkg')

print("Anki package 'CloudComputingFlashcards.apkg' has been generated. You can now import it into Anki.")