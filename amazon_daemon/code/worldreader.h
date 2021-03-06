#ifndef __WORLDREADER_H__
#define __WORLDREADER_H__
#include <exception>
#include <thread>
#include <iostream>
#include <pqxx/pqxx>
#include "safequeue.h"
#include "amazon.pb.h"
#include <google/protobuf/io/coded_stream.h>
#include <google/protobuf/io/zero_copy_stream_impl.h>

class Worldreader {
 private:
  SafeQueue<AResponses> &world_read_queue;
  std::thread mythread;
  bool is_active;
  int world_fd;
 public:
  Worldreader(SafeQueue<AResponses> &q, int world_fd);
  ~Worldreader();
  void wait_read(void);
  
  template<typename T>
    bool recvMesgFrom(T & message,
		      google::protobuf::io::FileInputStream * in ){
    google::protobuf::io::CodedInputStream input(in);
    uint32_t size;
    if (!input.ReadVarint32(&size)) {
      return false;
    }
    // Tell the stream not to read beyond that size.
    google::protobuf::io::CodedInputStream::Limit limit = input.PushLimit(size);
    // Parse the message.
    if (!message.MergeFromCodedStream(&input)) {
      return false;
    }
    if (!input.ConsumedEntireMessage()) {
      return false;
    }
    // Release the limit.
    input.PopLimit(limit);
    return true;
  }
};

#endif
