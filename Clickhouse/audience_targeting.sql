
create database test;

create table test.tag_user_bitmap
(
    tag_id String,
    user_bitmap AggregateFunction(groupBitmap, UInt32) comment 'User ID bitmap'
)
engine = MergeTree
order by tag_id;

insert into test.tag_user_bitmap values ('tag1', bitmapBuild(cast([1,2,3,4,5,6,7,8,9,10] as Array(UInt32)))),
    ('tag2', bitmapBuild(cast([6,7,8,9,10,11,12,13,14,15] as Array(UInt32)))),
    ('tag3', bitmapBuild(cast([2,4,6,8,10,12] as Array(UInt32))));

select groupBitmapAnd(user_bitmap) as user_count, bitmapToArray(groupBitmapAndState(user_bitmap)) as user_ids
from test.tag_user_bitmap 
where tag_id in ('tag1', 'tag2');
