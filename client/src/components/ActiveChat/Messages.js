import React, { useMemo } from 'react';
import { Box } from '@material-ui/core';
import { SenderBubble, OtherUserBubble } from '.';
import moment from 'moment';

const Messages = (props) => {
  const { messages, otherUser, userId } = props;

  // get the last read msg's index
  const lastReadRecieptIdx = useMemo(() => {
    return messages.reduceRight((prevIdx, msg, msgIdx) => {
      if(prevIdx === -1 && msg.isRead && msg.senderId === userId)
        return msgIdx; // found last message
      else
        return prevIdx; // carry over
    }, -1);
  }, [messages, userId]);

  return (
    <Box>
      {messages.map((message, idx) => {
        const time = moment(message.createdAt).format('h:mm');

        return message.senderId === userId ? (
          <SenderBubble
            otherUser={otherUser} 
            key={message.id} 
            text={message.text} 
            time={time}
            activeReadReceipt={idx===lastReadRecieptIdx}
          />
        ) : (
          <OtherUserBubble
            key={message.id}
            text={message.text}
            time={time}
            otherUser={otherUser}
          />
        );
      })}
    </Box>
  );
};

export default Messages;
