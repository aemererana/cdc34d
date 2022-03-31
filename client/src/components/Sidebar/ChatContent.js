import React, { useMemo } from "react";
import { Box, Chip, Typography } from "@material-ui/core";
import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles((theme) => ({
  root: {
    display: "flex",
    justifyContent: "space-between",
    marginLeft: 20,
    flexGrow: 1,
  },
  username: {
    fontWeight: "bold",
    letterSpacing: -0.2,
  },
  previewText: {
    fontSize: 12,
    color: "#9CADC8",
    letterSpacing: -0.17,
  },
  unreadMsg: {
    fontSize: 12,
    color: "#000",
    fontWeight: "bold",
    letterSpacing: -0.17,
  },
  unreadMsgCountChip: {
    marginRight: theme.spacing(1),
    marginTop: theme.spacing(1),
    fontSize: 10,
  },
}));

const ChatContent = ({ conversation }) => {
  const classes = useStyles();

  const { otherUser } = conversation;
  const latestMessageText = conversation.id && conversation.latestMessageText;

  // count unread msgs
  const unreadMsgCount = useMemo(() => {
    return conversation.messages.reduce(
      (prevCount, message) => 
        ((!message.isRead && message.senderId === conversation.otherUser.id) ? 
        ++prevCount : 
        prevCount), 
      0);
  }, [conversation]);

  return (
    <Box className={classes.root}>
      <Box>
        <Typography className={classes.username}>
          {otherUser.username}
        </Typography>
        <Typography className={(unreadMsgCount > 0) ? classes.unreadMsg : classes.previewText}>
          {latestMessageText}
        </Typography>
      </Box>
      { unreadMsgCount > 0 && (
        <Chip
          className={classes.unreadMsgCountChip}
          color="primary"
          size="small" 
          label={unreadMsgCount} 
        />
      )}
    </Box>
  );
};

export default ChatContent;
