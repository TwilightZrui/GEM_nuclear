from rosbag import Bag
import sys

with Bag('/home/twilight/dataset/221024_map_Lio_deepRobotics/LIO_data2/close_indoor_2_bpearl_time_sync.bag', 'w') as Y, Bag('/home/twilight/dataset/221024_map_Lio_deepRobotics/LIO_data2/close_indoor_2_bpearl.bag', 'r') as X:
    start_time = X.get_start_time()
    end_time = X.get_end_time()
    time_period = end_time - start_time
    for topic, msg, t in X:
        tCam1 = t
        time_for_now = float(t.secs)
        # print(time_for_now)
        # print(start_time)
        if topic == "/rslidar_points" or topic == "/ouster/points" or topic == "/ouster/imu":
            # if topic == "/rslidar_points"  or topic == "/velodyne_points" or topic == "/imu_data" :
            if topic == "/rslidar_points" or topic == "/ouster/points" or topic == "/ouster/imu":
                tCam1.secs = t.secs + 2
                tCam1.nsecs = t.nsecs
                if tCam1.nsecs <= 0:
                    tCam1.nsecs += 1000000000
                    tCam1.secs -= 1
                if tCam1.nsecs >= 1000000000:
                    tCam1.nsecs -= 1000000000
                    tCam1.secs += 1
                msg.header.stamp.secs = tCam1.secs
                msg.header.stamp.nsecs = tCam1.nsecs
                # print("Cam1:")
                # print(tCam1.secs,tCam1.nsecs,"       ",t.secs, t.nsecs,"    ",msg.header.stamp.secs,msg.header.stamp.nsecs)
                Y.write(topic, msg, tCam1)

            elif topic == "/tf":
                # if topic == "/rslidar_points"  or topic == "/velodyne_points" or topic == "/imu_data" :
                tCam1.secs = t.secs + 2
                tCam1.nsecs = t.nsecs
                if tCam1.nsecs <= 0:
                    tCam1.nsecs += 1000000000
                    tCam1.secs -= 1
                if tCam1.nsecs >= 1000000000:
                    tCam1.nsecs -= 1000000000
                    tCam1.secs += 1
                msg.transforms[0].header.stamp.secs = tCam1.secs + 2.35
                msg.transforms[0].header.stamp.nsecs = tCam1.nsecs
                # print("Cam1:")
                #print(tCam1.secs,tCam1.nsecs,"       ",t.secs, t.nsecs,"    ",msg.header.stamp.secs,msg.header.stamp.nsecs)
                Y.write(topic, msg, tCam1)

            elif topic == "/kitti/velo/pointcloud":
                msg.header.frame_id = "velodyne1"
                tCam1.secs = t.secs + 1576131367 - 1615709257
                tCam1.nsecs = t.nsecs + 553862 - 178740
                if tCam1.nsecs <= 0:
                    tCam1.nsecs += 1000000000
                    tCam1.secs -= 1
                if tCam1.nsecs >= 1000000000:
                    tCam1.nsecs -= 1000000000
                    tCam1.secs += 1
                msg.header.stamp.secs = tCam1.secs
                msg.header.stamp.nsecs = tCam1.nsecs
                # print("Cam1:")
                #print(tCam1.secs,tCam1.nsecs,"       ",t.secs, t.nsecs,"    ",msg.header.stamp.secs,msg.header.stamp.nsecs)
                Y.write(topic, msg, tCam1)

            elif topic == "/icp_odom":
                msg.header.frame_id = "velodyne1"
                tCam1.secs = t.secs + 1576131367-1576131508
                tCam1.nsecs = t.nsecs + 553862 - 29777
                if tCam1.nsecs <= 0:
                    tCam1.nsecs += 1000000000
                    tCam1.secs -= 1
                if tCam1.nsecs >= 1000000000:
                    tCam1.nsecs -= 1000000000
                    tCam1.secs += 1
                msg.header.stamp.secs = tCam1.secs
                msg.header.stamp.nsecs = tCam1.nsecs
                # print("Cam1:")
                #print(tCam1.secs,tCam1.nsecs,"       ",t.secs, t.nsecs,"    ",msg.header.stamp.secs,msg.header.stamp.nsecs)
                Y.write(topic, msg, tCam1)
                #print("Others",t.secs, t.nsecs)
            time = time_for_now-start_time
            print(time/time_period)

            sys.stdout.write("\033[F")  # back to previous line
            sys.stdout.write("\033[K")  # clear line
