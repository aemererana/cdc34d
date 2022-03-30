import React from 'react';
import { Box } from '@material-ui/core';
import { SenderBubble, OtherUserBubble } from '.';
import moment from 'moment';

const Messages = (props) => {
  const { messages, otherUser, userId } = props;

  const lastReadRecieptIdx = messages.map(elm => elm.isRead && elm.senderId === userId).lastIndexOf(true);

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
