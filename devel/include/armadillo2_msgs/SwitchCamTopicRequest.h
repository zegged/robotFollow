// Generated by gencpp from file armadillo2_msgs/SwitchCamTopicRequest.msg
// DO NOT EDIT!


#ifndef ARMADILLO2_MSGS_MESSAGE_SWITCHCAMTOPICREQUEST_H
#define ARMADILLO2_MSGS_MESSAGE_SWITCHCAMTOPICREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace armadillo2_msgs
{
template <class ContainerAllocator>
struct SwitchCamTopicRequest_
{
  typedef SwitchCamTopicRequest_<ContainerAllocator> Type;

  SwitchCamTopicRequest_()
    : num(0)  {
    }
  SwitchCamTopicRequest_(const ContainerAllocator& _alloc)
    : num(0)  {
  (void)_alloc;
    }



   typedef int16_t _num_type;
  _num_type num;





  typedef boost::shared_ptr< ::armadillo2_msgs::SwitchCamTopicRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::armadillo2_msgs::SwitchCamTopicRequest_<ContainerAllocator> const> ConstPtr;

}; // struct SwitchCamTopicRequest_

typedef ::armadillo2_msgs::SwitchCamTopicRequest_<std::allocator<void> > SwitchCamTopicRequest;

typedef boost::shared_ptr< ::armadillo2_msgs::SwitchCamTopicRequest > SwitchCamTopicRequestPtr;
typedef boost::shared_ptr< ::armadillo2_msgs::SwitchCamTopicRequest const> SwitchCamTopicRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::armadillo2_msgs::SwitchCamTopicRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::armadillo2_msgs::SwitchCamTopicRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace armadillo2_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg'], 'actionlib_msgs': ['/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg'], 'trajectory_msgs': ['/opt/ros/kinetic/share/trajectory_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'armadillo2_msgs': ['/home/zeged/catkin_ws/src/armadillo2/armadillo2_msgs/msgs', '/home/zeged/catkin_ws/devel/share/armadillo2_msgs/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::armadillo2_msgs::SwitchCamTopicRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::armadillo2_msgs::SwitchCamTopicRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::armadillo2_msgs::SwitchCamTopicRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::armadillo2_msgs::SwitchCamTopicRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::armadillo2_msgs::SwitchCamTopicRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::armadillo2_msgs::SwitchCamTopicRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::armadillo2_msgs::SwitchCamTopicRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "79e2a05b252e69632375170571b25d3d";
  }

  static const char* value(const ::armadillo2_msgs::SwitchCamTopicRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x79e2a05b252e6963ULL;
  static const uint64_t static_value2 = 0x2375170571b25d3dULL;
};

template<class ContainerAllocator>
struct DataType< ::armadillo2_msgs::SwitchCamTopicRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "armadillo2_msgs/SwitchCamTopicRequest";
  }

  static const char* value(const ::armadillo2_msgs::SwitchCamTopicRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::armadillo2_msgs::SwitchCamTopicRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int16 num\n\
";
  }

  static const char* value(const ::armadillo2_msgs::SwitchCamTopicRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::armadillo2_msgs::SwitchCamTopicRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.num);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct SwitchCamTopicRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::armadillo2_msgs::SwitchCamTopicRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::armadillo2_msgs::SwitchCamTopicRequest_<ContainerAllocator>& v)
  {
    s << indent << "num: ";
    Printer<int16_t>::stream(s, indent + "  ", v.num);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ARMADILLO2_MSGS_MESSAGE_SWITCHCAMTOPICREQUEST_H
